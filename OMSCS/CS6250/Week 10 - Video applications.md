---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-07-24
last_edited: 2024-07-24
draft: false
tags:
  - OMSCS
type: lecture
week: 10
---
# Week 10 - Video applications

## Additional reading

### Important Readings

VoIP: A comprehensive survey on a promising technology  
[https://www.sciencedirect.com/science/article/abs/pii/S1389128609001200Links to an external site.](https://www.sciencedirect.com/science/article/abs/pii/S1389128609001200)

MPEG: A Video Compression Standard for Multimedia Application  
[https://dl.acm.org/doi/pdf/10.1145/103085.103090Links to an external site.](https://dl.acm.org/doi/pdf/10.1145/103085.103090)

The JPEG Compression standard  
[https://ieeexplore.ieee.org/document/125072Links to an external site.](https://ieeexplore.ieee.org/document/125072)

JPEG File Interchange Format  
[https://www.w3.org/Graphics/JPEG/jfif3.pdfLinks to an external site.](https://www.w3.org/Graphics/JPEG/jfif3.pdf)

Watching Video over the Web: Part 1: Streaming Protocols  
[https://ieeexplore.ieee.org/document/5677508Links to an external site.](https://ieeexplore.ieee.org/document/5677508)

A Quest for an Internet Video: Quality-of-Experience Metric  
[https://www.cs.cmu.edu/~xia/resources/Documents/Balachandran-hotnets2012.pdfLinks to an external site.](https://www.cs.cmu.edu/~xia/resources/Documents/Balachandran-hotnets2012.pdf)

Confused, Timid, and Unstable: Picking a Video Streaming Rate is Hard  
[https://dl.acm.org/doi/pdf/10.1145/2398776.2398800Links to an external site.](https://dl.acm.org/doi/pdf/10.1145/2398776.2398800)

### Book References

Kurose-Ross Edition 7, Chapter 9

## Basic requirements

Sounds and video are interesting internet applications due to their interesting requirements. First they have far higher [[Bit|bit]]-rates than other applications.

![[media_bit_rates.png]]

Where facebook is someone flicking through 1 picture per second. 

Whilst video does have a much larger bit-rate you may be ok with skipping [[Bit|bits]] or there being a slight delay - in contrast with voice where skipped  [[Bit|bits]] or delayed audio may make the stream unusable. Therefore they have different dynamics at play.

There are three different types of multi-media applications we will look at:
1. Streaming stored audio/video,
	- This requires to play before the whole file is downloaded.
	- It is interactive skipping forward, pausing going backward.
	- It should have continuous playout i.e. play out as it was recorded without freezing.
2. Conversational audio/video, and
	- Multiple users connecting to the same stream.
	- These are highly delay sensitive - normally 150ms is a bench mark to being acceptable. 
	- They are loss-tolerant. i.e. it is ok if there is a small skip or small sections are scrambled.  
3. Live audio/video.
	- This is similar to streamed but you have a one to many dynamic.
	- The users are geographically displaced.
	- They are very delay sensitive. 

## [[Voice over IP (VoIP)]]

![[Voice over IP (VoIP)|VoIP]]

[[Voice over IP (VoIP)|VoIP]] faces unique challenges as the [[Internet]] is best effort delivery and does not come with built in quality of service gaurentees. Moveover, audio is an analogue form so any [[Voice over IP (VoIP)|VoIP]] will need to send a digital approximation.

- **Encoding**: We normally encode sound by making lots of descrete apprximations of the waves current position this is call **[[Quantization|quantization]]**. There are different categories of encoding schemes, narrowband, broadband, and multimode these each have different trade offs. The encoding hopes to make speech intelligible but also use as little bandwidth as possible.
- **Signalling**: Traditionally this takes care of how calls are set up and torn down. [[Protocol (networks)|Protocols]] such as [[Session Initiation Protocol (SIP)]] had handle this in [[Voice over IP (VoIP)|VoIP]] applications. This has four major responsibilities.
	1. User location - the parties finding one another,
	2. Session establishment - handling the callee accepting, rejecting or redirecting the call,
	3. Session negotiation - endpoint synchronizing on the same standard,
	4. Call participation management - handling people joining or leaving.
	
## Quality of service metrics

There are 3 major quality of service metrics in [[Voice over IP (VoIP)|VoIP]]:
- **End to end delay**: The total time between speaking and hearing.
- **Jitter**: Scrambled or jumpy audio and video.
- **Packet loss**: The amount of missing data there is at the end of the call.

## End to end 

This includes:
- the time it takes to encode the audio,
- the time it takes to put it in packets, 
- all the normal sources of network delay that network traffic encounters such as queueing delays, 
- “playback delay,” which comes from the receiver’s playback buffer (which is a mitigation technique for delay jitter, which we’ll be discussing next),
- and decoding delay, which is the time it takes to reconstruct the signal.

Delay is very important to the end user to stop people talking over one another. Below displays the acceptable levels.

![[e2e_delay.png]]

## Jitter

Due to the [[Internet]] having unreliable network times - packets will be received in a different order than they were sent out. We call this phenomenon *jitter*. This is problematic for [[Voice over IP (VoIP)|VoIP]] as we need to reconstruct a audio signal that has continuous playout - gaps in audio must be kept to less that 30-75ms.

The main way to handle this is keeping a playout buffer or jitter window. This delays the playout on the receivers side to wait to collect all packets before playing out. This has a payoff, the longer you wait the less Jitter but the more end-to-end delay. The less you wait the more Jitter and packet loss.

## Packet loss

Due to the use of the [[Internet|internet]] packet loss is inevitable in [[Voice over IP (VoIP)|VoIP]]. However, [[Voice over IP (VoIP)|VoIP]] uses an even tougher definition of packet loss - which is either it is lost or it arrives after the jitter window. Luckily [[Voice over IP (VoIP)|VoIP]] can tolerate between 1-20% packet loss depending on voice codex used.

To avoid packet loss we might want to use [[Transmission Control Protocol (TCP)|TCP]] however due to the tougher definition the transmission of packets might arrive after the jitter window so be considered lost anyway. Therefore most [[Voice over IP (VoIP)|VoIP]] applications use [[User Datagram Protocol (UDP)|UDP]] and just accept some packet loss - this lowers bandwidth usage as well.

There are 3 major techniques to handle packet loss in [[Voice over IP (VoIP)|VoIP]]

### Forward Error Correction

This transmits redundant data that can fill any gaps. This increases the bandwidth used but decreases packet loss. This can be done in a few different ways:
- Breaking the data into chunks that are overlapping - then we can use xor to reconstruct the data.
- Transmitting a lower quality stream along side the high quality stream.
The more redundant data you send the more bandwidth you use. Also some of these techniques require you to wait longer before playing out increasing end-to-end delay.

![[fec_example.png]]

### Interleaving

This technique does not require additional data to be transmitted instead it breaks up the chunks of data so that the data in one chunk does not contain consecutive bits. That way a lost packet generate many small gaps not noticeable by the human ear. The pay off is having to wait longer to receive consecutive chunks which increases end-to-end delay. 

![[interleaving.png]]

### Error concealment

This involves filling in the gaps using the packets around it. There are two basic forms of this:
- Simply replacing missing gaps with the chunk from before. This is easy to implement and is fairly good in most circumstances.
- Interpolating from the chunks on either side. This is computationally more expensive but normally provides better estimates.

## Live/on demand streaming

Streaming media content over the Internet accounts for nearly 60-70% of the Internet traffic. There are two flavours will we talk about here:
1. Live streaming of events.
2. On demand streaming of videos already recorded.
Whilst there restrictions differ by focusing on 2 we learn a lot of the general principles that apply to 1. 

Generally on-demand video sharing follows the same common pattern.
![[streaming_infra.png]]

Most notably they will use [[Content delivery network (CDN)|CDN]] to distribute content to be closer to their users.

To render the stored content correctly we need to make sure we do not drop any packets. With streaming the content to the user flow control will be important too. [[Transmission Control Protocol (TCP)|TCP]] provides these out of the box - therefore it is a better match that [[User Datagram Protocol (UDP)|UDP]].

![[internet_picture.png]]

## How we got to [[Hyper Text Transfer Protocol (HTTP)|HTTP]]

When streaming platforms were originally envisioned they wanted all the intelligence to be kept in a stateful server - with the client doing minimal work. 

![[original_design.png]]

However, this would:
- Require providers to by specialist hardware.
- Handle state in a scalable service.
- Navigate firewalls and middleboxes.

Instead the [[Hyper Text Transfer Protocol (HTTP)|HTTP]] protocol was already well used and understood by network participants. Here the server can be stateless and just provide the content the client requests. This had the following advantages:
- Servers can be stateless.
- Providers could use already established [[Content delivery network (CDN)|CDNs]]
- [[Hyper Text Transfer Protocol (HTTP)|HTTP]] messages were already understood in firewalls and middleboxes.
This meant that the original plan was abandoned and people moved to [[Hyper Text Transfer Protocol (HTTP)|HTTP]].

![[video_application_logic.png]]

## Streaming vs progressive downloading

Downloading large parts of the video has a couple of downsides:
- The user often leaves halfway through leading to wasted bandwidth.
- The client will need to store the video in memory which from large segments will use a lot of it.

The other option is just in time streaming where you download the next segment the user is watching. As the internet has variable throughput this would create stalling with the video.

Therefore a hybrid approach is taken. We maintain a playout-buffer (normally 5 seconds) and switch between two states:
1. **Filling state**: When the playout buffer is empty we try to fill it quickly - for example when we start the video or skip ahead.
2. **Steady state**: With a large buffer we wait for that to drop to a lower limit and start downloading more of the video until we fill the buffer again. This switches from being in an ON/OFF state.

![[video_playout.png]]

## Handling variation

There is a lot of variation with playing videos:
- You might be streaming on a phone or  a 4k wide screen needing different [[Bit|bit]]-rates.
- You may be streaming on a fixed wired internet or over ropy airport wifi.
- You might be using your whole homes 1.5 Mbps internet or you may be sharing the internet with you sibling playing a game at the same time.

![[Bitrate]]

Therefore a single [[Bitrate|bitrate]] would not handle this . Therefore normally producers make encodings for different required [[Bitrate|bitrates]]for streaming, such as 250 kbps, 500 kbps, 1.5 Mbps, 3 Mbps. Then we us [[Bitrate adaption|bitrate adaption]] to adjust the provided quality to the user depending on network and device requirements. 

To find out these quality ranges and the URLs for each download - when clients first connect to a server they download a manifest file with details all this.

![[Dynamic Adaptive Streaming over HTTP (DASH)|DASH]]

## Quality of Service metrics

1. Low or no rebuffering: where the video stalls.
2. High video quality.
3. Low video quality variations: i.e. a change in the video quality caused by [[Bitrate adaption|bitrate adaption]].
4. Low startup latency: The time spent in the filling state.

These quality of service metrics are competing with eachother, for example having the best quality video at all points might mean you need to change the video quality regularly and might risk rebuffering. A larger buffer might reduce rebuffering chance but will make startup slower. To reduce the startup latency you could start with lower quality video. Therefore it is critical to understand the payoffs between them.

Now we have our output metrics lets see the inputs to the calculation.
- **Network throughput**: The [[Bitrate|bitrate]] your network can currently sustain. This is constantly changing.
- **Video buffer size**: The amount of buffer you currently have.

## Rate-based adaption

One simple way to calculate the video quality is to look at your current bandwidth $C(t)$ and divide it by the available [[Bitrate|bitrates]] $R(t)$ and find the largest one such that $C(t)/R(t) > 1$ that way we are filling our buffer when downloading.

![[throughput_based_adaption.png]]

The issue is forecasting what $C(t)$ will be in the future.

Practically this is done it two steps:
- **Estimation**: Guessing $C(t)$ by considering our past download rates.
- **Quantization**: Using the above formula to pick a bitrate but we find $C(t)/R(t) > 1 + c$ for some constant $c$.
The constant allows:
- Us to avoid unneeded re-buffering.
- Different encoding that may require higher [[Bitrate|bitrate]] for shorter periods.
- Application and [[Layer 4 Transport|Transport layer]] overhead.

When forecasting $C(t)$ we normally use a weighted average of the past [[Bitrate|bitrate]]. This can be sluggish to adapting to a fall in [[Bitrate|bitrate]] causing rebuffering. Though the bigger issue is with how this interacts with [[Transmission Control Protocol (TCP)|TCP]].

Suppose we are in the following competitive networking position where we have two clients using [[Transmission Control Protocol (TCP)|TCP]].

![[DASH_underestimation.png]]

Consider the scenario when a client is watching a video over a 5 Mbps link. 

The available bitrates are {375kbps, 560 kbps, 750kbps, 1050kbps, 1400kbps, 1750kbs}. Clearly, the client would end up streaming at 1.75 Mbps under rate-based adaptation.

Suppose the user initially starts with no competition then someone comes and downloads a larger file. They are both using [[Transmission Control Protocol (TCP)|TCP]] that should converge to a fair share - though this takes some time.

![[DASH_under_graph.png]]

What happens in this case it we incrementally step down to the lowest quality video as the [[Bitrate adaption|bitrate adaption]] and [[Transmission Control Protocol (TCP)|TCP]] congestion window work together to drive down the videos share of the network.

First note [[Dynamic Adaptive Streaming over HTTP (DASH)|DASH]] has an on off pattern as described above.

![[DASH_flow.png]]

Then if the congestion window is reset in the off period it can allow the competing flow take more network share and this causes [[Dynamic Adaptive Streaming over HTTP (DASH)|DASH]] to pick a lower [[Bitrate|bitrate]]. Though this spiral continues as then the competition take a larger network share in the gaps throttling [[Dynamic Adaptive Streaming over HTTP (DASH)|DASH]]'s [[Bitrate|bitrate]] again.

![[DASH_TCP_fail.png]]

This is a problem for [[Dynamic Adaptive Streaming over HTTP (DASH)|DASH]] so implementations have to try to handle this correctly.

## Buffer-based bitrate adaption

There is a competing strategy which varies the [[Bitrate|bitrate]] based on the buffer size. The avoids the need to predict the network speed.

![[buffer_size_bitrate_adaption.png]]

Though comes with its own challenges.


