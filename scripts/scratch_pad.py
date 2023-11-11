
import obsidian_helper.constants as constants
import obsidian_helper.read_obsidian as read_obsidian
import obsidian_helper.write_obsidian as write_obsidian

for file in read_obsidian.get_obsidian_files():
    # last_edited = datetime.date.fromtimestamp(os.path.getmtime(file))
    obsidian_file = read_obsidian.read_obsidian_file(str(file))
    # reported_last_edited = obsidian_file.metadata.get('last_edited', None)
    # if reported_last_edited is None or reported_last_edited != last_edited:
    #     obsidian_file.metadata['last_edited'] = last_edited
    if "chatgpt" in obsidian_file.metadata:
        del obsidian_file.metadata["chatgpt"]
    obsidian_file.metadata[constants.CHECKED_FIELD] = False
    write_obsidian.write_obsidian_file(obsidian_file)
