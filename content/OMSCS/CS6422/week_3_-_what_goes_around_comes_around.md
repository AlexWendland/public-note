---
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-18'
date_checked: '2026-06-18'
draft: true
last_edited: '2026-06-18'
tags:
  - OMSCS
title: 'Week 3 - What Goes Around Comes Around... And Around...'
type: lecture
week: 3
---

Paper: [What Goes Around Comes Around... And Around...](https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf) — Stonebraker & Pavlo, SIGMOD Record 2024.

A retrospective on 20 years of data modelling and DBMS architecture since the original 2005 "What Goes Around Comes Around." The central argument: every non-relational data model since 2005 has either died, become a permanent niche, or gradually converged toward SQL and the relational model. SQL absorbs the best ideas from challengers and keeps winning.

> [!note]
> The original 2005 paper covered hierarchical (IMS), network (CODASYL), entity-relationship, extended relational, semantic, object-oriented, object-relational, and XML. The conclusion was the same: the relational model with an extensible type system dominated all comers. This 2024 follow-up shows the pattern has continued.

# Part 1: Data Models & Query Languages

## MapReduce Systems

Google built MapReduce in 2003 as a point solution for periodic internet crawl processing. In relational terms, Map is a UDF performing computation/filtering and Reduce is a GROUP BY. The whole system runs a single query:

```sql
SELECT map() FROM crawl_table GROUP BY reduce()
```

There was no prescribed data model or query language — the Map/Reduce functions parsed raw files themselves.

**Systems**: Google MR → Yahoo! Hadoop (2005, open-source on HDFS) → Meta Hive (SQL on Hadoop) → Cloudera Impala (RDBMS on HDFS, bypassing Hadoop) → Meta Presto (replaced Hive) → Spark/Flink (added SQL interfaces).

**Verdict: Dead.** A 2009 benchmark showed data warehouses significantly outperformed Hadoop. Google formally killed MR in 2014. "MR's deficiencies were so significant that it could not be saved despite the adoption and enthusiasm from the developer community." HDFS clusters persist in enterprises only as legacy. The Hadoop vendors (Cloudera, Hortonworks, MapR) were left without a viable product.

**What survived**: MR's ideas around scalability, elasticity, and fault tolerance carried forward into distributed RDBMSs. MR also revived shared-disk architectures with disaggregated storage, giving rise to open-source file formats and data lakes.

---

## Key/Value Stores

The simplest possible model: `(key, blob)`. The DBMS is unaware of blob contents. Most KV DBMSs only support `get`/`set`/`delete` on single values.

**Systems**: Memcached (caching), Redis (caching + richer API), Amazon Dynamo (2007, persistent), BerkeleyDB, LevelDB, RocksDB (Meta, forked from LevelDB to replace InnoDB in MySQL), DynamoDB (evolved to JSON record store), Aerospike (also evolved to richer records).

**Verdict: Niche / transitioning.** KV stores are dangerous for complex applications: no secondary indexes, no joins, no schema enforcement — all pushed back to the application. "It is not trivial to re-engineer a KV store to make it support a complex data model, whereas RDBMSs easily emulate KV stores without any changes."

DynamoDB and Aerospike both evolved toward richer JSON-based record stores — converging toward the document model. RDBMSs may be a better initial choice since they offer a path forward as application complexity grows.

**Positive pattern**: Using embedded KV stores (RocksDB, WiredTiger) as the storage backend for full-featured DBMSs is a valid architectural pattern — lowers the engineering cost of writing a new DBMS.

---

## Document Databases

Records are hierarchies of field/value pairs with arbitrary nesting. JSON is the current standard (preceded by SGML and XML). Schema is optional ("schema-on-read" or "schema later").

**Systems**: MongoDB (most popular), CouchDB, Couchbase. By 2020, almost every NoSQL DBMS added a SQL interface: DynamoDB PartiQL, Cassandra CQL, Aerospike AQL, Couchbase SQL++, MongoDB Atlas SQL.

**Verdict: Converging with RDBMSs.** "Document DBMSs are essentially the same as object-oriented DBMSs from the 1980s and XML DBMSs from the late 1990s — same arguments, same problems."

The key argument for document DBMSs — removing ORM impedance mismatch via denormalization — is flawed:
1. If the join is not one-to-many, denormalization duplicates data.
2. Prejoins are not necessarily faster than joins.
3. There is no data independence.

SQL added a JSON type in 2016. "The differences between the two kinds of systems have diminished over time and should become nearly indistinguishable in the future."

> [!note]
> The paper attributes MongoDB's success partly to marketing: "inferior DBMS products have succeeded via strong marketing despite the existence of better options available at the time: Oracle did this in the 1980s, MySQL did this in the 2000s, and MongoDB did this in the 2010s."

---

## Column-Family / Wide-Column Databases

A reduction of the document model to only one level of nesting. Each record can have optional attributes and cells can contain arrays of values. Despite the name, this is **not** columnar storage.

**Systems**: Google BigTable (2004, original), Apache Cassandra (copied BigTable's model), Apache HBase (also copied BigTable). BigTable's own limitations (no joins, no secondary indexes) were faithfully reproduced. Both Cassandra and HBase later added SQL-like frontends (CQL, Apache Phoenix).

Google itself built MegaStore (an RDBMS on BigTable) and then Spanner (which started on BigTable but was later rewritten to remove BigTable remnants). "It is now the primary database for many of its internal applications."

**Verdict: Niche.** "Without Google, this paper would not be talking about this category." All critiques of the document model apply here equally. Google's internal evolution — from BigTable to Spanner — is the clearest possible signal.

---

## Text Search Engines

Inverted indexes over tokenised documents. The vector space model (bag-of-words, TF-IDF relevance) dates to the SMART system in the 1960s.

**Systems**: Elasticsearch and Solr (both built on Apache Lucene, the dominant underlying library). RDBMSs with built-in full-text search: Oracle, SQL Server, MySQL, PostgreSQL.

**Verdict: Useful but should be absorbed.** Elasticsearch and Solr have "none-to-limited transaction capabilities" — data corruption requires rebuilding the entire document index from scratch, causing significant downtime. PostgreSQL's full-text search "has improved recently and is generally on par with the special-purpose systems" with the added benefit of built-in transactions.

Three management patterns exist: (1) polystore — run Elasticsearch alongside a RDBMS with ETL; (2) use a RDBMS with text-search extensions; (3) polystore middleware (e.g. BigDAWG). "It would be valuable if RDBMSs had a better story for search so these would not have to be a separate product."

> [!note]
> Inverted-index search is also being supplanted by similarity search using ML-generated embeddings — the use case that drives vector databases.

---

## Array Databases

Multi-dimensional arrays as first-class data types. Natural for scientific data (satellite imagery, genomics, fluid dynamics, ML tensors). Initial work began in the 1980s.

**Systems**: Rasdaman (one of the oldest, still in development; heavily influenced SQL:2023 SQL/MDA), kdb+ (one of the oldest; later rebranded as a vector database), SciDB, TileDB. Popular file formats: HDF5, NetCDF. RDBMSs with array extensions: Oracle GeoRaster, Teradata.

**Verdict: Permanently niche.** No major cloud provider offers a hosted array DBMS — they see no sizable market. SQL has been adding array support incrementally: SQL:1999 (1D fixed-length), SQL:2003 (nested arrays), SQL:2023 SQL/MDA (true multi-dimensional, inspired by Rasdaman). "Scientific applications will continue to ignore RDBMSs in favor of bespoke array systems."

Data cubes for OLAP have been eclipsed by columnar RDBMSs, which offer better flexibility and lower engineering cost.

---

## Vector Databases

A simplification of the array model to one-dimensional rasters. Primary use case: storing ML-generated embeddings (BERT, etc.) and querying via approximate nearest neighbor (ANN) search.

**Systems**: Pinecone, Milvus, Weaviate (standalone vector DBMSs). Open-source libraries: pgvector (PostgreSQL), FAISS (Meta), DiskANN (Microsoft). By 2023, RDBMSs absorbed vector indexes: Oracle, SingleStore, Rockset, ClickHouse. Elasticsearch and Solr added vector search. kdb+ rebranded as a vector database.

**Verdict: A feature, not a new architecture.** "Vector DBMSs are essentially document-oriented DBMSs with specialized ANN indexes. Such indexes are a feature, not the foundation of a new system architecture."

After ChatGPT's launch in late 2022, it took less than one year for major RDBMSs to add vector search extensions — far faster than JSON support took to be absorbed from document DBMSs. Most vendors integrated an existing open-source library rather than building from scratch, confirming the low engineering lift.

"We anticipate that vector DBMSs will undergo the same evolution as document DBMSs by adding features to become more relational-like (SQL, transactions, extensibility). Meanwhile, relational incumbents will have added vector indexes to their already long list of features."

---

## Graph Databases

Two main representations: RDF and property graphs (a superset of RDF). The paper focuses on property graphs. The key observation: a graph is always simulable as two relational tables:

```sql
Node(node_id, node_data)
Edge(node_id_1, node_id_2, edge_data)
```

**Systems (OLTP)**: Neo4j (most popular; uses pointer-based edge storage like CODASYL; advantageous for long pointer-chasing traversals). **Systems (analytics)**: TigerGraph, JanusGraph, Giraph, Turi (GraphLab). **RDBMSs with graph extensions**: SQL Server, Oracle, Amazon Neptune ("a graph-oriented veneer on top of Aurora MySQL"), Apache AGE (OpenCypher on PostgreSQL). **SQL:2023 SQL/PGQ**: property graph queries as a proper SQL extension.

**Verdict: RDBMSs will win.** Multiple performance studies show graph simulation on RDBMSs outperforms graph DBMSs. DuckDB with SQL/PGQ outperforms a leading graph DBMS by up to 10×. "This trend will continue with further improvements in worst-case optimal joins and factorized execution algorithms."

For analytics workloads, the best strategy is to compress the graph into a space-efficient in-memory data structure on a single node. "All but the largest graph databases are probably best handled this way" — distributed graph algorithms rarely outperform single-node implementations due to communication costs.

Neo4j's pointer-chasing is legitimately faster than join-based traversal for long edge chains, but the market for pure long-chain traversal without other RDBMS features is small. "We do not expect specialized graph DBMSs to be a large market."

---

## Data Model Summary

| Category | Verdict |
|---|---|
| MapReduce | Dead. Legacy HDFS clusters remain. |
| Key/Value Stores | Niche or evolved into richer systems. |
| Document Databases | Converging with RDBMSs via SQL adoption. |
| Column-Family | Niche. Google itself moved to Spanner. |
| Text Search Engines | Useful polystore component; should be absorbed into RDBMSs. |
| Array Databases | Scientific niche; will remain separate from RDBMSs. |
| Vector Databases | Feature, not architecture; will be absorbed by RDBMSs. |
| Graph Databases | RDBMSs will provide competitive graph APIs. Small market for specialists. |

---

# Part 2: System Architectures

## Columnar Systems

Row stores are optimised for OLTP (fetch all columns of one row quickly). OLAP workloads read a small subset of columns across many rows — a poor fit for row-oriented storage.

Column storage benefits:
1. **Compression** — a column block contains a single value type with repeated bytes; far more compressible than mixed-type row blocks.
2. **Vectorised execution** — process a whole column at a time (SIMD-friendly inner loop), vs. Volcano-style row-at-a-time.
3. **Minimal overhead** — row stores carry ~20 bytes of per-record header (null tracking, versioning metadata); column stores do not.

**Systems**: Amazon Redshift, Google BigQuery, Snowflake (also introduced "serverless computing" for cloud-native DBMSs). All existing data warehouse vendors (Teradata, Vertica, etc.) converted their row-store offerings to column stores.

**Verdict: Clear winner for OLAP.** "Over the last two decades, all vendors active in the data warehouse market have converted their offerings from a row store to a column store." Unambiguous architectural advancement — no critique.

---

## Cloud Databases

Early cloud DBMSs repackaged on-premises systems into managed VMs with direct-attached storage. The key architectural shift: networking bandwidth grew much faster than disk bandwidth, making disaggregated storage (object stores like S3) attractive.

Benefits of disaggregated storage:
1. **Per-query elasticity** — add compute nodes dynamically without reshuffling data; separate hardware pools for storage vs. compute.
2. **Compute reassignment** — idle compute nodes can be reused for other tasks (vs. shared-nothing where nodes must always be online).
3. **Push computation into storage** — can run filtering/aggregation close to data.

Snowflake introduced "serverless computing" — the first cloud-native DBMS to expose true per-query elasticity.

**Verdict: Dominant future architecture.** "The cloud has profoundly impacted DBMSs, causing them to be completely re-architected." The authors note this is "what goes around comes around" — shared-disk is an old idea that failed historically, but faster networking makes it viable again. Time-sharing services were popular in the 1970s; cloud platforms are their modern equivalent.

"We do not foresee shared-nothing architectures resurfacing in the future."

> [!note]
> Business risk: open-source DBMSs (MongoDB, Elasticsearch) face the danger of being monetised by major cloud providers without compensation — leading to licence changes and public conflicts with Amazon.

---

## Data Lakes / Lakehouses

A departure from monolithic proprietary data warehouses: applications write files directly to a distributed object store (S3, GCS, Azure Blob), bypassing the DBMS. Lakehouse execution engines then query accumulated files in open formats.

**Key open formats**:
- **Apache Parquet** (Twitter/Cloudera) — most popular columnar disk-resident format. Borrows PAX compression and nested-data shredding.
- **Apache ORC** (Meta) — similar techniques, also very popular.
- **Apache Arrow** — in-memory binary format for zero-copy exchange between systems.

**Lakehouse table formats** (add transactional updates on top of object stores):
- **Delta Lake** (Databricks), **Apache Iceberg**, **Apache Hudi**.

**Execution engines**: Databricks, Dremio, PrestoDB (Meta), Trino.

**Verdict: The next decade's OLAP archetype.** "Cloud-based object storage using open-source formats will be the OLAP DBMS archetype for the next ten years."

Critique: "At first glance, a data lake seems like a terrible idea — allowing any application to write arbitrary files into a centralized repository without any governance is a recipe for integrity, discovery, and versioning problems." Lakehouse middleware (Iceberg, Delta) is necessary to add governance. Query optimisation is also harder without statistics on raw files — adaptive query processing becomes imperative.

Legacy OLAP vendors (Teradata, Vertica) have extended their DBMSs to read from object stores in response to pricing pressure.

---

## NewSQL Systems

In the late 2000s, NoSQL DBMSs could scale horizontally but lacked strong transactions. Existing RDBMSs couldn't natively scale across machines. NewSQL appeared in the early 2010s: NoSQL scalability + SQL + ACID.

**First wave (in-memory)**: VoltDB/H-Store, SingleStore (formerly MemSQL), HyPer, Microsoft Hekaton ("only available as an extension to a legacy DBMS, requiring the faster engine to use the slower DBMS's interfaces").

**Second wave (distributed transactional SQL)**: TiDB, CockroachDB, YugabyteDB, PlanetScale (based on Vitess).

**NoSQL reversals**: MongoDB, Cassandra, and DynamoDB all added ACID transactions — "despite previously strong claims that they were unnecessary." Google Spanner (2012) discarded eventual consistency in favour of real transactions.

**Verdict: Underdelivered.** "There has yet to be a dramatic uptake in NewSQL DBMS adoption." Companies are too risk-averse to migrate OLTP systems. The in-memory bet was wrong: flash storage drove down costs and latency while persistent memory (Intel Optane) collapsed. SSDs remain dominant for OLTP.

"They leverage new ideas but have yet to have the same impact as columnar and cloud DBMSs."

---

## Hardware Accelerators

A 50-year hunt for cost-effective DBMS hardware acceleration.

**1980s custom silicon** (all failed): Britton-Lee IDM/500, Teradata Y-net. "Targeted a small subset of the execution path, and was not cost-effective."

**FPGA-based**: Netezza (late 1990s, PostgreSQL fork); Swarm64 (abandoned FPGA before acquisition); Vitesse Deepgreen DB (only remaining FPGA DBMS from an ISV).

**GPU-based**: Kinetica, Sqream, Brytlyt, HeavyDB. Advantage: existing CUDA tooling. Disadvantage: bottlenecks on GPU memory size — if data doesn't fit, you spend all your time loading rather than computing.

**Cloud vendor custom silicon** (only viable path): Amazon Redshift AQUA, Google BigQuery custom components for in-memory shuffles.

**Verdict: Hyperscalers only.** "We do not see a use case for specialized hardware outside of the major cloud vendors." The business model is broken for third parties: the accelerator vendor needs a DBMS partner, but no DBMS vendor wants to outsource a critical component to an outside company. Cloud CPUs are extremely cheap at scale.

Only Amazon, Google, and Microsoft can justify the $50–100M R&D cost of custom hardware — and only they control the full hardware-software stack needed for deep integration.

---

## Blockchain Databases

Blockchains are decentralised log-structured databases (ledgers) maintaining incremental checksums via Merkle trees to ensure immutability. The ideal use case: peer-to-peer applications where no central authority can be trusted. BFT commit protocols determine transaction ordering.

**Systems**: Bitcoin (the only real use case today). DBMS attempts: Fluree, BigChainDB, ResilientDB. Amazon QLDB — provides immutability and verifiability without decentralisation (no BFT); "Amazon built QLDB after finding no compelling use case for a fully decentralised blockchain DBMS."

**Verdict: Harshest assessment in the paper.** "Legitimate businesses are unwilling to pay the performance price (about five orders of magnitude) to use a blockchain DBMS." Claims about data resiliency via replication in a peer-to-peer environment are called "meaningless": "No sensible company would rely on random participants on the Internet as the backup solution for mission-critical databases."

Damning observation: "All the major cryptocurrency exchanges run their businesses off traditional RDBMSs and not blockchain systems." Summary: "An inefficient technology looking for an application."

---

## Architecture Summary

| Category | Verdict |
|---|---|
| Columnar Systems | Revolutionised OLAP. All data warehouse vendors have converted. |
| Cloud Databases | Upended DBMS architecture. Shared-disk + disaggregated storage will dominate. |
| Data Lakes / Lakehouses | OLAP archetype for the next decade. Object stores + open formats. |
| NewSQL Systems | New ideas, lackluster adoption. In-memory bet was wrong. |
| Hardware Accelerators | Only viable for hyperscale cloud vendors. |
| Blockchain Databases | Inefficient technology looking for an application. |

---

# Parting Observations

**Marketing can carry bad products.** Oracle in the 1980s, MySQL in the 2000s, MongoDB in the 2010s each gained enough early traction to survive long enough to fix their engineering debt. The database market rewards early movers even when better alternatives exist.

**Beware DBMSs from non-DBMS companies.** Meta (Hive, Presto, Cassandra, RocksDB), LinkedIn (Kafka, Pinot), 10gen (MongoDB), PowerSet (HBase) all open-sourced in-house databases. These are almost always immature when first released — teams without DBMS expertise building systems where existing tools would suffice, partly because internal promotions favour engineers who build new systems.

**Out-of-box experience matters.** A major selling point of NoSQL was a better "first five minutes" than RDBMSs. DuckDB's rise is partly attributable to in-situ processing of local and cloud files without any setup. "Every DBMS should make it easy to perform in situ processing of local and cloud-storage files."

**NL interfaces won't replace SQL.** LLMs generating SQL from natural language are impressive but face old problems: English is ambiguous, LLM output is not explainable, and enterprises are reluctant to depend on LLMs for financial/decision-making data. NL interfaces are useful for initial exploratory query construction, not for OLTP applications. "Nobody will write OLTP applications using an NL, as most generate queries using ORMs."

**The community needs reusable components.** The paper calls for POSIX-like standards for DBMS internals to avoid repeated reimplementation of non-novel components. Positive signs: Parquet/ORC/Arrow (storage formats), Apache Calcite/Orca (query optimisation), DataFusion/Velox (execution engines).
