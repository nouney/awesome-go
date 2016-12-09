
### Extended Awesome Go

*Daily clone of [avelino/awesome-go](https://github.com/avelino/awesome-go) with information from [Go-Search](http://go-search.org).*

:arrow_down: - Number of packages that imports this package

:star:  - Number of stars

---

# Awesome Go [![Build Status](https://travis-ci.org/avelino/awesome-go.svg?branch=master)](https://travis-ci.org/avelino/awesome-go) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Join the chat at https://gitter.im/avelino/awesome-go](https://badges.gitter.im/avelino/awesome-go.svg)](https://gitter.im/avelino/awesome-go?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


A curated list of awesome Go frameworks, libraries and software. Inspired by [awesome-python](https://github.com/vinta/awesome-python).


### Contributing

Please take a quick gander at the [contribution guidelines](https://github.com/avelino/awesome-go/blob/master/CONTRIBUTING.md) first. Thanks to all [contributors](https://github.com/avelino/awesome-go/graphs/contributors); you rock!

#### *If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you!*


### Contents

- [Awesome Go](#awesome-go)
    - [Audio & Music](#audiomusic)
    - [Authentication & OAuth](#authentication--oauth)
    - [Command Line](#command-line)
    - [Configuration](#configuration)
    - [Continuous Integration](#continuous-integration)
    - [CSS Preprocessors](#css-preprocessors)
    - [Data Structures](#data-structures)
    - [Database](#database)
    - [Database Drivers](#database-drivers)
    - [Date & Time](#date--time)
    - [Distributed Systems](#distributed-systems)
    - [Email](#email)
    - [Embeddable Scripting Languages](#embeddable-scripting-languages)
    - [Financial](#financial)
    - [Forms](#forms)
    - [Game Development](#game-development)
    - [Generation & Generics](#generation--generics)
    - [Go Compilers](#go-compilers)
    - [Goroutines](#goroutines)
    - [GUI](#gui)
    - [Hardware](#hardware)
    - [Images](#images)
    - [Logging](#logging)
    - [Machine Learning](#machine-learning)
    - [Messaging](#messaging)
    - [Miscellaneous](#miscellaneous)
    - [Natural Language Processing](#natural-language-processing)
    - [Networking](#networking)
    - [OpenGL](#opengl)
    - [ORM](#orm)
    - [Package Management](#package-management)
    - [Query Language](#query-language)
    - [Resource Embedding](#resource-embedding)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Security](#security)
    - [Serialization](#serialization)
    - [Template Engines](#template-engines)
    - [Testing](#testing)
    - [Text Processing](#text-processing)
    - [Third-party APIs](#third-party-apis)
    - [Utilities](#utilities)
    - [Validation](#validation)
    - [Version Control](#version-control)
    - [Video](#video)
    - [Web Frameworks](#web-frameworks)
        - [Middlewares](#middlewares)
            - [Actual middlewares](#actual-middlewares)
            - [Libraries for creating HTTP middlewares](#libraries-for-creating-http-middlewares)
    - [Windows](#windows)

- [Tools](#tools)
    - [Code Analysis](#code-analysis)
    - [Editor Plugins](#editor-plugins)
    - [Go Tools](#go-tools)
    - [Software Packages](#software-packages)
        - [DevOps Tools](#devops-tools)
        - [Other Software](#other-software)

- [Server Applications](#server-applications)

- [Resources](#resources)
    - [Benchmarks](#benchmarks)
    - [Conferences](#conferences)
    - [E-Books](#e-books)
    - [Twitter](#twitter)
    - [Websites](#websites)
        - [Tutorials](#tutorials)


## Audio/Music

*Libraries for manipulating audio.*

* [flac](https://github.com/eaburns/flac) - A native Go FLAC decoder. - :arrow_down:3 - :star:52
* [flac](https://github.com/mewkiz/flac) - A native Go FLAC decoder. - :arrow_down:6 - :star:29
* [gaad](https://github.com/Comcast/gaad) - A native Go AAC bitstream parser - :arrow_down:0 - :star:11
* [go-sox](https://github.com/krig/go-sox) - libsox bindings for go. - :arrow_down:10 - :star:37
* [go_mediainfo](https://github.com/zhulik/go_mediainfo) - libmediainfo bindings for go. - :arrow_down:2 - :star:9
* [id3v2](https://github.com/bogem/id3v2) - Fast and stable ID3 parsing and writing library for Go - :arrow_down:1 - :star:8
* [mix](https://github.com/go-mix/mix) - Sequence-based Go-native audio mixer for music apps. - :arrow_down:5 - :star:40
* [mp3](https://github.com/tcolgate/mp3) - A native Go MP3 decoder. - :arrow_down:5 - :star:19
* [music-theory](https://github.com/go-music-theory/music-theory) - Music theory models in Go. - :arrow_down:0 - :star:120
* [PortAudio](https://github.com/gordonklaus/portaudio) - Go bindings for the PortAudio audio I/O library. - :arrow_down:51 - :star:63
* [portmidi](https://github.com/rakyll/portmidi) - Go bindings for PortMidi. - :arrow_down:34 - :star:93
* [taglib](https://github.com/wtolson/go-taglib) - Go bindings for taglib. - :arrow_down:18 - :star:44
* [vorbis](https://github.com/mccoyst/vorbis) - A "native" Go Vorbis decoder (uses CGO, but has no dependencies). - :arrow_down:0 - :star:9
* [waveform](https://github.com/mdlayher/waveform) - Go package capable of generating waveform images from audio streams. - :arrow_down:1 - :star:135


## Authentication & OAuth

*Libraries for implementing authentications schemes.*

* [authboss](https://github.com/go-authboss/authboss) - A modular authentication system for the web. It tries to remove as much boilerplate and "hard things" as possible so that each time you start a new web project in Go, you can plug it in, configure, and start building your app without having to build an authentication system each time. - :arrow_down:0 - :star:700
* [Go-AWS-Auth](https://github.com/smartystreets/go-aws-auth) - AWS (Amazon Web Services) request signing library. - :arrow_down:44 - :star:144
* [go-jose](https://github.com/square/go-jose) - A fairly complete implementation of the JOSE working group's JSON Web Token, JSON Web Signatures, and JSON Web Encryption specs. - :arrow_down:200 - :star:536
* [go-oauth2-server](https://github.com/RichardKnop/go-oauth2-server) - A standalone, specification-compliant,  OAuth2 server written in Golang. - :arrow_down:0 - :star:381
* [go.auth](https://github.com/bradrydzewski/go.auth) - Authentication API for Go web applications. - :arrow_down:51 - :star:326
* [gologin](https://github.com/dghubble/gologin) - chainable handlers for login with OAuth1 and OAuth2 authentication providers. - :arrow_down:35 - :star:647
* [gorbac](https://github.com/mikespook/gorbac) - provides a lightweight role-based access control (RBAC) implementation in Golang. - :arrow_down:7 - :star:401
* [goth](https://github.com/markbates/goth) - provides a simple, clean, and idiomatic way to use OAuth and OAuth2. Handles multiple provides out of the box. - :arrow_down:323 - :star:825
* [httpauth](https://github.com/goji/httpauth) - HTTP Authentication middleware. - :arrow_down:39 - :star:102
* [jwt](https://github.com/robbert229/jwt) - A clean and easy to use implmentatino of JSON Web Tokens (JWT). - :arrow_down:2 - :star:0
* [jwt-go](https://github.com/dgrijalva/jwt-go) - Golang implementation of JSON Web Tokens (JWT). - :arrow_down:1494 - :star:1459
* [oauth2](https://github.com/golang/oauth2) - Successor of goauth2. Generic OAuth 2.0 package that comes with JWT, Google APIs, Compute Engine and App Engine support. - :arrow_down:60 - :star:854
* [osin](https://github.com/RangelReale/osin) - Golang OAuth2 server library. - :arrow_down:306 - :star:959
* [permissions2](https://github.com/xyproto/permissions2) - Library for keeping track of users, login states and permissions. Uses secure cookies and bcrypt. - :arrow_down:18 - :star:176
* [yubigo](https://github.com/GeertJohan/yubigo) - a Yubikey client package that provides a simple API to integrate the Yubico Yubikey into a go application. - :arrow_down:7 - :star:63


## Command Line


### Standard CLI

*Libraries for building standard or basic Command Line applications*

* [cli](https://github.com/mkideal/cli) - A feature-rich and easy to use command-line package based on golang tag - :arrow_down:42 - :star:204
* [cli-init](https://github.com/tcnksm/gcli) - The easy way to start building Golang command line application. - :arrow_down:0 - :star:559
* [climax](http://github.com/tucnak/climax) - An alternative CLI with "human face", in spirit of Go command - :arrow_down:6 - :star:98
* [cobra](https://github.com/spf13/cobra) - A Commander for modern Go CLI interactions - :arrow_down:3764 - :star:2817
* [docopt.go](https://github.com/docopt/docopt.go) - A command-line arguments parser that will make you smile. - :arrow_down:54 - :star:723
* [drive](https://github.com/odeke-em/drive) - Google Drive client for the commandline
* [go-arg](https://github.com/alexflint/go-arg) - Struct-based argument parsing in Go - :arrow_down:34 - :star:370
* [go-flags](https://github.com/jessevdk/go-flags) - go command line option parser - :arrow_down:1065 - :star:623
* [kingpin](https://github.com/alecthomas/kingpin) - A command line and flag parser supporting sub commands. - :arrow_down:131 - :star:732
* [liner](https://github.com/peterh/liner) - A Go readline-like library for command-line interfaces. - :arrow_down:337 - :star:325
* [mitchellh/cli](https://github.com/mitchellh/cli) - A Go library for implementing command-line interfaces. - :arrow_down:1585 - :star:460
* [mow.cli](https://github.com/jawher/mow.cli) - A Go library for building CLI applications with sophisticated flag and argument parsing and validation. - :arrow_down:129 - :star:367
* [readline](https://github.com/chzyer/readline) - A pure golang implementation that provide most of features in GNU-Readline under MIT license. - :arrow_down:109 - :star:634
* [ukautz/clif](https://github.com/ukautz/clif) - A small command line interface framework. - :arrow_down:2 - :star:69
* [urfave/cli](https://github.com/urfave/cli) - A simple, fast, and fun package for building command line apps in Go (formerly codegangsta/cli). - :arrow_down:590 - :star:4621
* [wlog](https://github.com/dixonwille/wlog) - A simple logging interface that supports cross-platform color and concurrency. - :arrow_down:4 - :star:5
* [wmenu](https://github.com/dixonwille/wmenu) - An easy to use menu structure for cli applications that prompts users to make choices. - :arrow_down:0 - :star:7


### Advanced Console UIs

*Libraries for building Console Applications and Console User Interfaces*

* [aurora](https://github.com/logrusorgru/aurora) - ANSI terminal colors that supports fmt.Printf/Sprintf - :arrow_down:0 - :star:199
* [chalk](https://github.com/ttacon/chalk) - Intuitive package for prettifying terminal/console output. - :arrow_down:113 - :star:169
* [color](https://github.com/fatih/color) - Versatile package for colored terminal output. - :arrow_down:1114 - :star:1081
* [colourize](https://github.com/TreyBastian/colourize) - Go library for ANSI colour text in terminals. - :arrow_down:1 - :star:8
* [go-colortext](https://github.com/daviddengcn/go-colortext) - Go library for color output in terminals. - :arrow_down:207 - :star:148
* [gocui](https://github.com/jroimartin/gocui) - Minimalist Go library aimed at creating Console User Interfaces. - :arrow_down:63 - :star:777
* [gommon/color](https://github.com/labstack/gommon/tree/master/color) - Style terminal text.
* [termbox-go](https://github.com/nsf/termbox-go) - Termbox is a library for creating cross-platform text-based interfaces. - :arrow_down:819 - :star:1603
* [termtables](https://github.com/apcera/termtables) - A Go port of the Ruby library [terminal-tables](https://github.com/tj/terminal-table) for simple ASCII table generation as well as providing markdown and HTML output - :arrow_down:17 - :star:64
* [termui](https://github.com/gizak/termui) - Go terminal dashboard based on **termbox-go** and inspired by [blessed-contrib](https://github.com/yaronn/blessed-contrib). - :arrow_down:122 - :star:5091
* [uilive](https://github.com/gosuri/uilive) - A library for updating terminal output in realtime. - :arrow_down:21 - :star:465
* [uiprogress](https://github.com/gosuri/uiprogress) - A flexible library to render progress bars in terminal applications. - :arrow_down:40 - :star:831
* [uitable](https://github.com/gosuri/uitable) - A library to improve readability in terminal apps using tabular data. - :arrow_down:57 - :star:347


## Configuration

*Libraries for configuration parsing*

* [config](https://github.com/olebedev/config) - JSON or YAML configuration wrapper with environment variables and flags parsing. - :arrow_down:56 - :star:81
* [configure](https://github.com/paked/configure) - Provides configuration through multiple sources, including JSON, flags and environment variables. - :arrow_down:13 - :star:20
* [env](https://github.com/caarlos0/env) - Parse environment variables to Go structs (with defaults). - :arrow_down:25 - :star:162
* [envcfg](https://github.com/tomazk/envcfg) - Un-marshaling environment variables to Go structs. - :arrow_down:1 - :star:79
* [envconf](https://github.com/ian-kent/envconf) - Configuration from environment - :arrow_down:11 - :star:3
* [envconfig](https://github.com/vrischmann/envconfig) - Read your configuration from environment variables. - :arrow_down:12 - :star:93
* [gcfg](https://github.com/go-gcfg/gcfg) - read INI-style configuration files into Go structs; supports user-defined types and subsections
* [gofigure](https://github.com/ian-kent/gofigure) - Go application configuration made easy - :arrow_down:10 - :star:36
* [hjson](https://github.com/hjson/hjson-go) - Human JSON, a configuration file format for humans. Relaxed syntax, fewer mistakes, more comments. - :arrow_down:2 - :star:51
* [ingo](https://github.com/schachmat/ingo) - Flags persisted in an ini-like config file - :arrow_down:5 - :star:10
* [ini](https://github.com/go-ini/ini) - Go package for read and write INI files - :arrow_down:147 - :star:370
* [mini](https://github.com/FogCreek/mini) - A golang package for parsing ini-style configuration files - :arrow_down:5 - :star:80
* [store](https://github.com/tucnak/store) - A lightweight configuration manager for Go - :arrow_down:0 - :star:202
* [viper](https://github.com/spf13/viper) - Go configuration with fangs - :arrow_down:3338 - :star:1947

## Continuous Integration

*Tools for help with continuous integration*

* [drone](https://github.com/drone/drone) - Drone is a Continuous Integration platform built on Docker, written in Go
* [goveralls](https://github.com/mattn/goveralls) - Go integration for Coveralls.io continuous code coverage tracking system. - :arrow_down:0 - :star:285
* [overalls](https://github.com/go-playground/overalls) - Multi-Package go project coverprofile for tools like goveralls - :arrow_down:0 - :star:27

## CSS Preprocessors

*Libraries for preprocessing CSS files*

* [c6](https://github.com/c9s/c6) - High performance SASS compatible-implementation compiler written in Go - :arrow_down:0 - :star:322
* [gcss](https://github.com/yosssi/gcss) - Pure Go CSS Preprocessor. - :arrow_down:17 - :star:356
* [go-libsass](https://github.com/wellington/go-libsass) - Go wrapper to the 100% Sass compatible libsass project. - :arrow_down:24 - :star:36

## Data Structures

*Generic datastructures and algorithms in Go.*

* [binpacker](https://github.com/zhuangsirui/binpacker) - Binary packer and unpacker helps user build custom binary stream. - :arrow_down:1 - :star:24
* [bitset](https://github.com/willf/bitset) - Go package implementing bitsets. - :arrow_down:128 - :star:210
* [bloom](https://github.com/zhenjl/bloom) - Bloom filters implemented in Go. - :arrow_down:11 - :star:87
* [boomfilters](https://github.com/tylertreat/BoomFilters) - Probabilistic data structures for processing continuous, unbounded streams - :arrow_down:12 - :star:736
* [count-min-log](https://github.com/seiflotfy/count-min-log) - A Go implementation Count-Min-Log sketch: Approximately counting with approximate counters (Like Count-Min sketch but using less memory). - :arrow_down:1 - :star:23
* [cuckoofilter](https://github.com/seiflotfy/cuckoofilter) - Cuckoo filter: a good alternative to a counting bloom filter implemented in Go. - :arrow_down:5 - :star:186
* [encoding](https://github.com/zhenjl/encoding) - Integer Compression Libraries for Go. - :arrow_down:0 - :star:46
* [go-adaptive-radix-tree](https://github.com/plar/go-adaptive-radix-tree) - A Go implementation of Adaptive Radix Tree. - :arrow_down:1 - :star:10
* [go-datastructures](https://github.com/Workiva/go-datastructures) - A collection of useful, performant, and thread-safe data structures - :arrow_down:0 - :star:2716
* [go-geoindex](https://github.com/hailocab/go-geoindex) - In-memory geo index. - :arrow_down:9 - :star:201
* [gods](https://github.com/emirpasic/gods) - Go Data Structures. Containers, Sets, Lists, Stacks, Maps, BidiMaps, Trees, HashSet etc.
* [golang-set](https://github.com/deckarep/golang-set) - Thread-Safe and Non-Thread-Safe high-performance sets for Go. - :arrow_down:149 - :star:419
* [goskiplist](https://github.com/ryszard/goskiplist) - A skip list implementation in Go.
* [hilbert](https://github.com/google/hilbert) - Go package for mapping values to and from space-filling curves, such as Hilbert and Peano curves. - :arrow_down:2 - :star:35
* [levenshtein](https://github.com/agnivade/levenshtein) - Implementation to calculate levenshtein distance in Go. - :arrow_down:2 - :star:5
* [mafsa](https://github.com/smartystreets/mafsa) - MA-FSA implementation with Minimal Perfect Hashing - :arrow_down:14 - :star:214
* [roaring](https://github.com/RoaringBitmap/roaring) - Go package implementing compressed bitsets. - :arrow_down:11 - :star:154
* [skiplist](https://github.com/gansidui/skiplist) - Skiplist implementation in Go - :arrow_down:0 - :star:30
* [trie](https://github.com/derekparker/trie) - Trie implementation in Go - :arrow_down:1 - :star:142
* [ttlcache](https://github.com/diegobernardes/ttlcache) - An in-memory LRU string-interface{} map with expiration for golang - :arrow_down:0 - :star:31
* [willf/bloom](https://github.com/willf/bloom) - Go package implementing Bloom filters. - :arrow_down:54 - :star:251

## Database

*Databases implemented in Go.*


* [BigCache](https://github.com/allegro/bigcache) - Efficient key/value cache for gigabytes of data. - :arrow_down:12 - :star:774
* [bolt](https://github.com/boltdb/bolt) - A low-level key/value database for Go. - :arrow_down:1897 - :star:4737
* [buntdb](https://github.com/tidwall/buntdb) - A fast, embeddable, in-memory key/value database for Go with custom indexing and spatial support. - :arrow_down:12 - :star:1048
* [cache2go](https://github.com/muesli/cache2go) - An in-memory key:value cache which supports automatic invalidation based on timeouts. - :arrow_down:22 - :star:110
* [cockroach](https://github.com/cockroachdb/cockroach) - A Scalable, Geo-Replicated, Transactional Datastore - :arrow_down:0 - :star:7668
* [couchcache](https://github.com/codingsince1985/couchcache) - A RESTful caching micro-service backed by Couchbase server. - :arrow_down:0 - :star:15
* [dgraph](https://github.com/dgraph-io/dgraph) - Scalable, Distributed, Low Latency, High Throughput Graph Database.
* [diskv](https://github.com/peterbourgon/diskv) - A home-grown disk-backed key-value store. - :arrow_down:81 - :star:386
* [eliasdb](https://github.com/krotik/eliasdb) - Dependency-free, transactional graph database with REST API, phrase search and SQL-like query language.
* [forestdb](https://github.com/couchbase/goforestdb) - Go bindings for ForestDB. - :arrow_down:10 - :star:22
* [GCache](https://github.com/bluele/gcache) - Cache library with support for expirable Cache, LFU, LRU and ARC. - :arrow_down:15 - :star:115
* [geocache](https://github.com/melihmucuk/geocache) - An in-memory cache that is suitable for geolocation based applications. - :arrow_down:0 - :star:47
* [go-cache](https://github.com/pmylund/go-cache) - An in-memory key:value store/cache (similar to Memcached) library for Go, suitable for single-machine applications. - :arrow_down:165 - :star:620
* [goleveldb](https://github.com/syndtr/goleveldb) - An implementation of the [LevelDB](https://github.com/google/leveldb) key/value database in the Go.
* [groupcache](https://github.com/golang/groupcache) - Groupcache is a caching and cache-filling library, intended as a replacement for memcached in many cases. - :arrow_down:92 - :star:4747
* [influxdb](https://github.com/influxdb/influxdb) - Scalable datastore for metrics, events, and real-time analytics - :arrow_down:601 - :star:8728
* [ledisdb](https://github.com/siddontang/ledisdb) - Ledisdb is a high performance NoSQL like Redis based on LevelDB.
* [levigo](https://github.com/jmhodges/levigo) - Levigo is a Go wrapper for LevelDB. - :arrow_down:141 - :star:276
* [pREST](https://github.com/nuveo/prest) - Serve a RESTful API from any PostgreSQL database.
* [prometheus](https://github.com/prometheus/prometheus) - Monitoring system and time series database.
* [rqlite](https://github.com/rqlite/rqlite) - Replicated SQLite, using Raft consensus. - :arrow_down:0 - :star:1870
* [tidb](https://github.com/pingcap/tidb) - TiDB is a distributed SQL database. Inspired by the design of Google F1. - :arrow_down:94 - :star:4651
* [tiedot](https://github.com/HouzuoGuo/tiedot) - Your NoSQL database powered by Golang. - :arrow_down:0 - :star:1609
* [Tile38](https://github.com/tidwall/tile38) - A geolocation DB with spatial index and realtime geofencing.

*Database schema migration.*

* [goose](https://github.com/steinbacher/goose) - Database migration tool. You can manage your database's evolution by creating incremental SQL or Go scripts. - :arrow_down:1 - :star:17
* [gormigrate](https://github.com/go-gormigrate/gormigrate) - Database schema migration helper for Gorm ORM. - :arrow_down:0 - :star:9
* [migrate](https://github.com/mattes/migrate) - Database migration handling in Golang support MySQL,PostgreSQL,Cassandra and SQLite. - :arrow_down:0 - :star:735
* [pravasan](https://github.com/pravasan/pravasan) - Simple Migration tool - currently for MySQL but planning to support soon for Postgres, SQLite, MongoDB, etc., - :arrow_down:0 - :star:12
* [sql-migrate](https://github.com/rubenv/sql-migrate) - Database migration tool. Allows embedding migrations into the application using go-bindata. - :arrow_down:117 - :star:497

*Database tools.*

* [go-mysql](https://github.com/siddontang/go-mysql) - A go toolset to handle MySQL protocol and replication.
* [go-mysql-elasticsearch](https://github.com/siddontang/go-mysql-elasticsearch) - Sync your MySQL data into Elasticsearch automatically.
* [kingshard](https://github.com/flike/kingshard) - kingshard is a high performance proxy for MySQL powered by Golang.
* [myreplication](https://github.com/2tvenom/myreplication) - MySql binary log replication listener. Support statement and row based replication. - :arrow_down:0 - :star:58
* [orchestrator](https://github.com/outbrain/orchestrator) - MySQL replication topology manager & visualizer
* [pgweb](https://github.com/sosedoff/pgweb) - A web-based PostgreSQL database browser - :arrow_down:0 - :star:3630
* [vitess](https://github.com/youtube/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services. - :arrow_down:0 - :star:3923

*SQL query builder, libraries for building and using SQL.*

* [dat](https://github.com/mgutz/dat) - Go Postgres Data Access Toolkit - :arrow_down:2 - :star:357
* [Dotsql](https://github.com/gchaincl/dotsql) - Go library that helps you keep sql files in one place and use it with ease. - :arrow_down:6 - :star:237
* [goqu](https://github.com/doug-martin/goqu) - An idiomatic SQL builder and query library. - :arrow_down:10 - :star:266
* [igor](https://github.com/galeone/igor) - Abstraction layer for PostgreSQL that supports advanced functionality and uses gorm-like syntax. - :arrow_down:3 - :star:53
* [ozzo-dbx](https://github.com/go-ozzo/ozzo-dbx) - Powerful data retrieval methods as well as DB-agnostic query building capabilities. - :arrow_down:2 - :star:108
* [scaneo](https://github.com/variadico/scaneo) - Generate Go code to convert database rows into arbitrary structs. - :arrow_down:0 - :star:79
* [sqrl](https://github.com/elgris/sqrl) - SQL query builder, fork of Squirrel with improved performance. - :arrow_down:2 - :star:45
* [Squirrel](https://github.com/Masterminds/squirrel) - Go library that helps you build SQL queries. - :arrow_down:61 - :star:904
* [xo](https://github.com/knq/xo) - Generate idiomatic Go code for databases based on existing schema definitions or custom queries supporting PostgreSQL, MySQL, SQLite, Oracle, and Microsoft SQL Server. - :arrow_down:0 - :star:723


## Database Drivers

*Libraries for connecting and operating databases.*

* Relational Databases
    * [bgc](https://github.com/viant/bgc) - Datastore Connectivity for BigQuery for go. - :arrow_down:0 - :star:0
    * [firebirdsql](https://github.com/nakagami/firebirdsql) - Firebird RDBMS SQL driver for Go - :arrow_down:4 - :star:46
    * [go-adodb](https://github.com/mattn/go-adodb) - Microsoft ActiveX Object DataBase driver for go that using database/sql. - :arrow_down:61 - :star:40
    * [go-bqstreamer](https://github.com/rounds/go-bqstreamer) - BigQuery fast and concurrent stream insert. - :arrow_down:0 - :star:111
    * [go-mssqldb](https://github.com/denisenkom/go-mssqldb) - Microsoft MSSQL driver prototype in go language. - :arrow_down:172 - :star:395
    * [go-oci8](https://github.com/mattn/go-oci8) - Oracle driver for go that using database/sql. - :arrow_down:54 - :star:157
    * [go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) - MySQL driver for Go. - :arrow_down:4548 - :star:2669
    * [go-sqlite3](https://github.com/mattn/go-sqlite3) - SQLite3 driver for go that using database/sql. - :arrow_down:2600 - :star:1408
    * [gofreetds](https://github.com/minus5/gofreetds) Microsoft MSSQL driver. Go wrapper over [FreeTDS](http://www.freetds.org). - :arrow_down:1 - :star:39
    * [pgx](https://github.com/jackc/pgx) - PostgreSQL driver supporting features beyond those exposed by database/sql. - :arrow_down:152 - :star:684
    * [pq](https://github.com/lib/pq) - Pure Go Postgres driver for database/sql. - :arrow_down:3535 - :star:2324

* NoSQL Databases
    * [aerospike-client-go](https://github.com/aerospike/aerospike-client-go) - Aerospike client in Go language. - :arrow_down:173 - :star:182
    * [arangolite](https://github.com/solher/arangolite) - Lightweight golang driver for ArangoDB. - :arrow_down:6 - :star:34
    * [asc](https://github.com/viant/asc) - Datastore Connectivity for Aerospike for go. - :arrow_down:0 - :star:1
    * [cayley](https://github.com/google/cayley) - A graph database with support for multiple backends. - :arrow_down:18 - :star:8622
    * [dsc](https://github.com/viant/dsc) - Datastore connectivity for SQL, NoSQL, structured files. - :arrow_down:4 - :star:1
    * [dynago](https://github.com/underarmour/dynago) - Dynago is a principle of least surprise client for DynamoDB - :arrow_down:1 - :star:18
    * [go-couchbase](https://github.com/couchbase/go-couchbase) - Couchbase client in Go - :arrow_down:197 - :star:217
    * [go-couchdb](https://github.com/fjl/go-couchdb) - Yet another CouchDB HTTP API wrapper for Go - :arrow_down:17 - :star:35
    * [gocb](https://github.com/couchbase/gocb) - Official Couchbase Go SDK - :arrow_down:19 - :star:183
    * [gocql](http://gocql.github.io) - A Go language driver for Apache Cassandra.
    * [gomemcache](https://github.com/bradfitz/gomemcache/) - memcache client library for the Go programming language.
    * [gorethink](https://github.com/dancannon/gorethink) - Go language driver for RethinkDB - :arrow_down:338 - :star:1024
    * [goriak](https://github.com/zegl/goriak) - Go language driver for Riak KV - :arrow_down:0 - :star:1
    * [mgo](https://godoc.org/labix.org/v2/mgo) - MongoDB driver for the Go language that implements a rich and well tested selection of features under a very simple API following standard Go idioms.
    * [neo4j](https://github.com/cihangir/neo4j) - Neo4j Rest API Bindings for Golang - :arrow_down:0 - :star:15
    * [Neo4j-GO](https://github.com/davemeehan/Neo4j-GO) - Neo4j REST Client in golang. - :arrow_down:4 - :star:63
    * [neoism](https://github.com/jmcvetta/neoism) - Neo4j client for Golang - :arrow_down:97 - :star:271
    * [redigo](https://github.com/garyburd/redigo) - Redigo is a Go client for the Redis database.
    * [redis](https://github.com/go-redis/redis) - Redis client for Golang - :arrow_down:7 - :star:1105
    * [redis](https://github.com/hoisie/redis) - A simple, powerful Redis client for Go. - :arrow_down:82 - :star:514
    * [redis](https://github.com/bsm/redeo) - Redis-protocol compatible TCP servers/services. - :arrow_down:4 - :star:107

* Search and Analytic Databases
    * [bleve](https://github.com/blevesearch/bleve) - A modern text indexing library for go. - :arrow_down:499 - :star:2796
    * [elastic](https://github.com/olivere/elastic) - Elasticsearch client for Go. - :arrow_down:70 - :star:827
    * [elastigo](https://github.com/mattbaird/elastigo) - A Elasticsearch client library. - :arrow_down:1 - :star:799
    * [goes](https://github.com/belogik/goes) - A library to interact with Elasticsearch. - :arrow_down:47 - :star:72
    * [skizze](https://github.com/seiflotfy/skizze) - A probabilistic data-structures service and storage.

## Date & Time

*Libraries for working with dates and times.*

* [carbon](https://github.com/uniplaces/carbon) - A simple Time extension with a lot of util methods, ported from PHP Carbon library. - :arrow_down:2 - :star:45
* [durafmt](https://github.com/hako/durafmt) - A time duration formatting library for Go. - :arrow_down:1 - :star:124
* [go-persian-calendar](https://github.com/yaa110/go-persian-calendar) - The implementation of the Persian (Solar Hijri) Calendar in Go (golang).
* [goweek](https://github.com/grsmv/goweek) - Library for working with week entity in golang. - :arrow_down:1 - :star:7
* [now](https://github.com/jinzhu/now) - Now is a time toolkit for golang. - :arrow_down:91 - :star:701
* [NullTime](https://github.com/kirillDanshin/nulltime) - Nullable time.Time - :arrow_down:0 - :star:1
* [timeutil](https://github.com/leekchan/timeutil) - Useful extensions (Timedelta, Strftime, ...) to the golang's time package. - :arrow_down:2 - :star:110


## Distributed Systems

*Packages that help with building Distributed Systems.*

* [celeriac](https://github.com/svcavallar/celeriac.v1) - A library for adding support for interacting and monitoring Celery workers, tasks and events in Go
* [flowgraph](https://github.com/vectaport/flowgraph) - MPI-style ready-send coordination layer. - :arrow_down:4 - :star:19
* [glow](https://github.com/chrislusf/glow) - Easy-to-Use scalable distributed big data processing, Map-Reduce, DAG execution, all in pure Go. - :arrow_down:0 - :star:1210
* [go-jump](https://github.com/dgryski/go-jump) - A port of Google's "Jump" Consistent Hash function. - :arrow_down:5 - :star:84
* [gorpc](https://github.com/valyala/gorpc) - Simple, fast and scalable RPC library for high load. - :arrow_down:12 - :star:275
* [grpc-go](https://github.com/grpc/grpc-go) - The Go language implementation of gRPC. HTTP/2 based RPC. - :arrow_down:0 - :star:2391
* [hprose](https://github.com/hprose/hprose-golang) - A very newbility RPC Library, support 25+ languages now. - :arrow_down:0 - :star:22
* [jsonrpc](https://github.com/osamingo/jsonrpc) - The jsonrpc package helps implement of JSON-RPC 2.0. - :arrow_down:0 - :star:9
* [jsonrpc](https://github.com/ybbus/jsonrpc) - A JSON-RPC 2.0 HTTP client implementation
* [micro](https://github.com/micro/micro) - A pluggable microservice toolkit and distributed systems platform. - :arrow_down:0 - :star:2352
* [NATS](https://github.com/nats-io/gnatsd) - A lightweight, high performance messaging system for microservices, IoT, and cloud native systems. - :arrow_down:0 - :star:2327
* [raft](https://github.com/hashicorp/raft) - Golang implementation of the Raft consensus protocol, by HashiCorp. - :arrow_down:437 - :star:759
* [raft](https://github.com/coreos/etcd/tree/master/raft#readme) - Go implementation of the Raft consensus protocol, by CoreOS.
* [ringpop-go](https://github.com/uber/ringpop-go) - Scalable, fault-tolerant application-layer sharding for Go applications - :arrow_down:12 - :star:179
* [rpcx](https://github.com/smallnest/rpcx) - A distributed pluggable RPC service framework like alibaba Dubbo. - :arrow_down:4 - :star:268
* [sleuth](https://github.com/ursiform/sleuth) - A library for master-less p2p auto-discovery and RPC between HTTP services (using [ZeroMQ](https://github.com/zeromq/libzmq)). - :arrow_down:0 - :star:188
* [tendermint](https://github.com/tendermint/tendermint) - High-performance middleware for transforming a state machine written in any programming language into a Byzantine Fault Tolerant replicated state machine using the Tendermint consensus and blockchain protocols.
* [torrent](https://github.com/anacrolix/torrent) - BitTorrent client package. - :arrow_down:65 - :star:1325
    * [dht](https://godoc.org/github.com/anacrolix/torrent/dht) - BitTorrent Kademlia DHT implementation.
    * [go-peerflix](https://github.com/Sioro-Neoku/go-peerflix) - Video streaming torrent client. - :arrow_down:0 - :star:203

## Email

*Libraries that implement email creation and sending*

* [douceur](https://github.com/aymerick/douceur) - CSS inliner for your HTML emails. - :arrow_down:0 - :star:64
* [email](https://github.com/jordan-wright/email) - A robust and flexible email library for Go. - :arrow_down:91 - :star:701
* [go-dkim](https://github.com/toorop/go-dkim) - A DKIM library, to sign & verify email. - :arrow_down:2 - :star:20
* [go-imap](https://github.com/emersion/go-imap) - An IMAP library for clients and servers - :arrow_down:26 - :star:122
* [Gomail](https://github.com/go-gomail/gomail/) - Gomail is a very simple and powerful package to send emails.
* [Hectane](https://github.com/hectane/hectane) - Lightweight SMTP client providing an HTTP API - :arrow_down:0 - :star:72
* [MailHog](https://github.com/mailhog/MailHog) - Email and SMTP testing with web and API interface - :arrow_down:0 - :star:1198
* [SendGrid](https://github.com/sendgrid/sendgrid-go) - SendGrid's Go library for sending email - :arrow_down:94 - :star:211
* [smtp](https://github.com/mailhog/smtp) - SMTP server protocol state machine - :arrow_down:10 - :star:25



## Embeddable Scripting Languages

*Embedding other languages inside your go code*

* [agora](https://github.com/PuerkitoBio/agora) - Dynamically typed, embeddable programming language in Go - :arrow_down:0 - :star:241
* [anko](https://github.com/mattn/anko) - Scriptable interpreter written in Go
* [gisp](https://github.com/jcla1/gisp) - Simple LISP in Go - :arrow_down:0 - :star:333
* [go-duktape](https://github.com/olebedev/go-duktape) - Duktape JavaScript engine bindings for Go - :arrow_down:14 - :star:390
* [go-lua](https://github.com/Shopify/go-lua) - A port of the Lua 5.2 VM to pure Go - :arrow_down:50 - :star:737
* [go-php](https://github.com/deuill/go-php) - PHP bindings for Go - :arrow_down:0 - :star:186
* [go-python](https://github.com/sbinet/go-python) - naive go bindings to the CPython C-API - :arrow_down:29 - :star:411
* [golua](https://github.com/aarzilli/golua) - Go bindings for Lua C API
* [gopher-lua](https://github.com/yuin/gopher-lua) - a Lua 5.1 VM and compiler written in Go - :arrow_down:211 - :star:1317
* [ngaro](https://github.com/db47h/ngaro) - Embeddable Ngaro VM implementation enabling scripting in Retro
* [otto](https://github.com/robertkrimen/otto) - A JavaScript interpreter written in Go - :arrow_down:581 - :star:2409
* [purl](https://github.com/ian-kent/purl) - Perl 5.18.2 embedded in Go - :arrow_down:0 - :star:13


## Financial

*Packages for accounting and finance*

* [accounting](https://github.com/leekchan/accounting) - money and currency formatting for golang - :arrow_down:4 - :star:221
* [decimal](https://github.com/shopspring/decimal) - Arbitrary-precision fixed-point decimal numbers - :arrow_down:465 - :star:321
* [vat](https://github.com/dannyvankooten/vat) - VAT number validation & EU VAT rates - :arrow_down:0 - :star:28


## Forms

*Libraries for working with forms.*

* [bind](https://github.com/robfig/bind)  - Bind form data to any Go values - :arrow_down:0 - :star:14
* [binding](https://github.com/mholt/binding) - Binds form and JSON data from net/http Request to struct. - :arrow_down:83 - :star:510
* [conform](https://github.com/leebenson/conform) - Keeps user input in check. Trims, sanitizes & scrubs data based on struct tags. - :arrow_down:4 - :star:34
* [form](https://github.com/go-playground/form) - Decodes url.Values into Go value(s) and Encodes Go value(s) into url.Values. Dual Array and Full map support. - :arrow_down:5 - :star:132
* [formam](https://github.com/monoculum/formam) - decode form's values into a struct. - :arrow_down:5 - :star:63
* [forms](https://github.com/albrow/forms) - A framework-agnostic library for parsing and validating form/JSON data which supports multipart forms and files. - :arrow_down:7 - :star:63
* [gorilla/csrf](https://github.com/gorilla/csrf) - CSRF protection for Go web applications & services. - :arrow_down:42 - :star:136
* [nosurf](https://github.com/justinas/nosurf) - A CSRF protection middleware for Go. - :arrow_down:97 - :star:667


## Game Development

*Awesome game development libraries.*

* [Ebiten](https://github.com/hajimehoshi/ebiten) - A simple SNES-like 2D game library in Go - :arrow_down:65 - :star:151
* [engo](https://github.com/EngoEngine/engo) - Engo is an open-source 2D game engine written in Go. It follows the Entity-Component-System paradigm. - :arrow_down:0 - :star:290
* [GarageEngine](https://github.com/vova616/GarageEngine) - 2d game engine written in Go working on OpenGL. - :arrow_down:0 - :star:238
* [glop](https://github.com/runningwild/glop) - Glop (Game Library Of Power) is a fairly simple cross-platform game library.
* [go-astar](https://github.com/beefsack/go-astar) - Go implementation of the A\* path finding algorithm - :arrow_down:3 - :star:156
* [go-collada](https://github.com/GlenKelley/go-collada) - Go package for working with the Collada file format. - :arrow_down:9 - :star:9
* [go-sdl2](https://github.com/veandco/go-sdl2) - Go bindings for the [Simple DirectMedia Layer](https://www.libsdl.org/).
* [go3d](https://github.com/ungerik/go3d) - A performance oriented 2D/3D math package for Go - :arrow_down:0 - :star:112
* [gonet](https://github.com/xtaci/gonet) - A game server skeleton implemented with golang
* [Leaf](https://github.com/name5566/leaf) - A lightweight game server framework - :arrow_down:1 - :star:787
* [termloop](https://github.com/JoelOtter/termloop) - Terminal-based game engine for Go, built on top of Termbox - :arrow_down:21 - :star:658


## Generation & Generics

*Tools to enhance the language with features like generics via code generation*

* [efaceconv](https://github.com/t0pep0/efaceconv) - Code generation tool for high performance conversion from interface{} to immutable type without allocations
* [gen](https://github.com/clipperhouse/gen) - Code generation tool for ‘generics’-like functionality. - :arrow_down:0 - :star:731
* [go-linq](https://github.com/ahmetalpbalkan/go-linq) - .NET LINQ-like query methods for Go. - :arrow_down:21 - :star:828
* [interfaces](https://github.com/rjeczalik/interfaces) - Command line tool for generating interface definitions. - :arrow_down:2 - :star:78
* [pkgreflect](https://github.com/ungerik/pkgreflect) - A Go preprocessor for package scoped reflection. - :arrow_down:0 - :star:39


## Go Compilers

*Tools for compiling Go to other languages*

* [gopherjs](https://github.com/gopherjs/gopherjs) - A compiler from Go to JavaScript. - :arrow_down:0 - :star:4209
* [llgo](https://github.com/go-llvm/llgo) - LLVM-based compiler for Go.
* [tardisgo](https://github.com/tardisgo/tardisgo) - Golang to Haxe to CPP/CSharp/Java/JavaScript transpiler. - :arrow_down:0 - :star:316


## Goroutines

*Tools for managing and working with Goroutines*
* [go-flow](https://github.com/kamildrazkiewicz/go-flow) - Control goroutines execution order. - :arrow_down:0 - :star:2
* [goworker](https://github.com/benmanns/goworker) - goworker is a Go-based background worker - :arrow_down:17 - :star:1484
* [grpool](https://github.com/ivpusic/grpool) - Lightweight Goroutine pool. - :arrow_down:2 - :star:123
* [pool](https://github.com/go-playground/pool) - a limited consumer goroutine or unlimited goroutine pool for easier goroutine handling and cancellation. - :arrow_down:0 - :star:220
* [tunny](https://github.com/Jeffail/tunny) - A goroutine pool for golang. - :arrow_down:1 - :star:379


## GUI

*Libraries for building GUI Applications*

* [go-gtk](http://mattn.github.io/go-gtk/) - Go bindings for GTK
* [go-qml](https://github.com/go-qml/qml) - QML support for the Go language - :arrow_down:1 - :star:1703
* [goqt](https://github.com/visualfc/goqt) - Golang bindings to the Qt cross-platform application framework.
* [gosx-notifier](https://github.com/deckarep/gosx-notifier) - OSX Desktop Notifications library for Go. - :arrow_down:22 - :star:310
* [gotk3](https://github.com/gotk3/gotk3) - Go bindings for GTK3.
* [qt](https://github.com/therecipe/qt) - Qt binding for Go (support for Windows / macOS / Linux / Android / iOS / Sailfish OS / Raspberry Pi) - :arrow_down:22 - :star:179
* [sciter](https://github.com/oskca/sciter) - Go bindings for Sciter: the Embeddable HTML/CSS/script engine for modern desktop UI development. - :arrow_down:21 - :star:369
* [systray](https://github.com/getlantern/systray) - Cross platform Go library to place an icon and menu in the notification area - :arrow_down:12 - :star:107
* [trayhost](https://github.com/shurcooL/trayhost) - Cross-platform Go library to place an icon in the host operating system's taskbar. - :arrow_down:1 - :star:66
* [ui](https://github.com/andlabs/ui) - Platform-native GUI library for Go. - :arrow_down:50 - :star:3288
* [walk](https://github.com/lxn/walk) - Windows application library kit for Go.


## Hardware

*Libraries, tools, and tutorials for interacting with hardware.*

See [go-hardware](https://github.com/rakyll/go-hardware) for a comprehensive list.

## Images

*Libraries for manipulating images.*

* [bild](https://github.com/anthonynsimon/bild) - A collection of image processing algorithms in pure Go.
* [bimg](https://github.com/h2non/bimg) - Small package for fast and efficient image processing using libvips. - :arrow_down:3 - :star:185
* [geopattern](https://github.com/pravj/geopattern) - Create beautiful generative image patterns from a string. - :arrow_down:11 - :star:867
* [gg](https://github.com/fogleman/gg) - 2D rendering in pure Go. - :arrow_down:28 - :star:665
* [gift](https://github.com/disintegration/gift) - Package of image processing filters. - :arrow_down:62 - :star:813
* [go-cairo](https://github.com/ungerik/go-cairo) - Go binding for the cairo graphics library. - :arrow_down:27 - :star:54
* [go-gd](https://github.com/bolknote/go-gd) - Go binding for GD library. - :arrow_down:11 - :star:39
* [go-nude](https://github.com/koyachi/go-nude) - Nudity detection with Go. - :arrow_down:5 - :star:188
* [go-opencv](https://github.com/lazywei/go-opencv) - Go bindings for OpenCV. - :arrow_down:0 - :star:443
* [go-webcolors](https://github.com/jyotiska/go-webcolors) - Port of webcolors library from Python to Go. - :arrow_down:8 - :star:18
* [imagick](https://github.com/gographics/imagick) - Go binding to ImageMagick's MagickWand C API.
* [imaginary](https://github.com/h2non/imaginary) - Fast and simple HTTP microservice for image resizing. - :arrow_down:0 - :star:820
* [imaging](https://github.com/disintegration/imaging) - Simple Go image processing package. - :arrow_down:269 - :star:875
* [img](https://github.com/hawx/img) - A selection of image manipulation tools. - :arrow_down:0 - :star:80
* [ln](https://github.com/fogleman/ln) - 3D line art rendering in Go.
* [mpo](https://github.com/donatj/mpo) - A decoder and conversion tool for MPO 3D Photos. - :arrow_down:1 - :star:3
* [picfit](https://github.com/thoas/picfit) - An image resizing server written in Go. - :arrow_down:0 - :star:518
* [pt](https://github.com/fogleman/pt) - A path tracing engine written in Go. - :arrow_down:0 - :star:952
* [resize](https://github.com/nfnt/resize) - Image resizing for the Go with common interpolation methods. - :arrow_down:700 - :star:1150
* [rez](https://github.com/bamiaux/rez) - Image resizing in pure Go and SIMD. - :arrow_down:10 - :star:119
* [smartcrop](https://github.com/muesli/smartcrop) - Finds good crops for arbitrary images and crop sizes. - :arrow_down:2 - :star:304
* [svgo](https://github.com/ajstarks/svgo) - Go Language Library for SVG generation. - :arrow_down:347 - :star:766
* [tga](https://github.com/ftrvxmtrx/tga) - Package tga is a TARGA image format decoder/encoder. - :arrow_down:3 - :star:13

## Logging

*Libraries for generating and working with log files.*

* [glog](https://github.com/golang/glog) - Leveled execution logs for Go. - :arrow_down:20730 - :star:1073
* [go-log](https://github.com/siddontang/go-log) - Log lib supports level and multi handlers.
* [go-log](https://github.com/ian-kent/go-log) - A log4j implementation in Go. - :arrow_down:0 - :star:19
* [go-logger](https://github.com/apsdehal/go-logger) - Simple logger of Go Programs, with level handlers. - :arrow_down:15 - :star:159
* [gologger](https://github.com/sadlil/gologger) - Simple easy to use log lib for go, logs in Colored Cosole, Simple Console, File or Elasticsearch. - :arrow_down:0 - :star:20
* [gone/log](https://github.com/One-com/gone/tree/master/log#readme) - Fast, extendable, full-featured, std-lib source compatible log library.
* [log](https://github.com/apex/log) - Structured logging package for Go. - :arrow_down:390 - :star:303
* [log](https://github.com/go-playground/log) - Simple, configurable and scalable Structured Logging for Go. - :arrow_down:50 - :star:193
* [log-voyage](https://github.com/firstrow/logvoyage) - Full-featured logging saas written in golang. - :arrow_down:0 - :star:61
* [log15](https://github.com/inconshreveable/log15) - Simple, powerful logging for Go - :arrow_down:166 - :star:506
* [logex](https://github.com/chzyer/logex) - An golang log lib, supports tracking and level, wrap by standard log lib - :arrow_down:20 - :star:26
* [logger](https://github.com/azer/logger) - Minimalistic logging library for Go. - :arrow_down:21 - :star:68
* [logrus](https://github.com/Sirupsen/logrus) - a structured logger for Go. - :arrow_down:29949 - :star:3335
* [logrusly](https://github.com/sebest/logrusly) - [logrus](https://github.com/sirupsen/logrus) plug-in to send errors to a [Loggly](https://www.loggly.com/). - :arrow_down:14 - :star:13
* [logutils](https://github.com/hashicorp/logutils) - Utilities for slightly better logging in Go (Golang) extending the standard logger. - :arrow_down:532 - :star:139
* [logxi](https://github.com/mgutz/logxi) - A 12-factor app logger that is fast and makes you happy. - :arrow_down:0 - :star:219
* [lumberjack](https://github.com/natefinch/lumberjack) - Simple rolling logger, implements io.WriteCloser. - :arrow_down:19 - :star:343
* [mlog](https://github.com/jbrodriguez/mlog) - A simple logging module for go, with 5 levels, an optional rotating logfile feature and stdout/stderr output. - :arrow_down:2 - :star:5
* [ozzo-log](https://github.com/go-ozzo/ozzo-log) - High performance logging supporting log severity, categorization, and filtering. Can send filtered log messages to various targets (e.g. console, network, mail). - :arrow_down:0 - :star:59
* [seelog](https://github.com/cihub/seelog) -   logging functionality with flexible dispatching, filtering, and formatting. - :arrow_down:888 - :star:732
* [slf](https://github.com/ventu-io/slf) - The Structured Logging Facade (SLF) for Go (like SLF4J but structured and for Go) - :arrow_down:33 - :star:29
* [slog](https://github.com/ventu-io/slog) - The reference implementation of the Structured Logging Facade (SLF) for Go - :arrow_down:10 - :star:21
* [stdlog](https://github.com/alexcesaro/log) - Stdlog is an object-oriented library providing leveled logging. It is very useful for cron jobs. - :arrow_down:73 - :star:37
* [tail](https://github.com/hpcloud/tail) - A Go package striving to emulate the features of the BSD tail program. - :arrow_down:98 - :star:595
* [xlog](https://github.com/rs/xlog) - A structured logger for `net/context` aware HTTP handlers with flexible dispatching. - :arrow_down:29 - :star:92
* [zap](https://github.com/uber-go/zap) - Fast, structured, leveled logging in Go. - :arrow_down:108 - :star:1149

## Machine Learning

*Libraries for Machine Learning.*

* [bayesian](https://github.com/jbrukh/bayesian) - Naive Bayesian Classification for Golang. - :arrow_down:26 - :star:367
* [CloudForest](https://github.com/ryanbressler/CloudForest) - Fast, flexible, multi-threaded ensembles of decision trees for machine learning in pure Go. - :arrow_down:48 - :star:388
* [gago](https://github.com/MaxHalford/gago) - Multi-population, flexible, parallel genetic algorithm. - :arrow_down:12 - :star:148
* [go-fann](https://github.com/white-pony/go-fann) - Go bindings for Fast Artificial Neural Networks(FANN) library. - :arrow_down:7 - :star:75
* [go-galib](https://github.com/thoj/go-galib) - Genetic Algorithms library written in Go / golang - :arrow_down:11 - :star:130
* [go-pr](https://github.com/daviddengcn/go-pr) - Pattern recognition package in Go lang. - :arrow_down:0 - :star:42
* [gobrain](https://github.com/goml/gobrain) - Neural Networks written in go - :arrow_down:3 - :star:115
* [godist](https://github.com/e-dard/godist) - Various probability distributions, and associated methods. - :arrow_down:0 - :star:11
* [goga](https://github.com/tomcraven/goga) - Genetic algorithm library for Go. - :arrow_down:2 - :star:43
* [GoLearn](https://github.com/sjwhitworth/golearn) - General Machine Learning library for Go. - :arrow_down:0 - :star:3201
* [golinear](https://github.com/danieldk/golinear) - liblinear bindings for Go - :arrow_down:5 - :star:28
* [goml](https://github.com/cdipaolo/goml) - On-line Machine Learning in Go
* [goRecommend](https://github.com/timkaye11/goRecommend) - Recommendation Algorithms library written in Go.
* [gorgonia](https://github.com/chewxy/gorgonia) - graph-based computational library like Theano for Go that provides primitives for building various machine learning and neural network algorithms. - :arrow_down:1 - :star:679
* [libsvm](https://github.com/datastream/libsvm) - libsvm golang version derived work based on LIBSVM 3.14. - :arrow_down:0 - :star:43
* [mlgo](https://github.com/NullHypothesis/mlgo) - This project aims to provide minimalistic machine learning algorithms in Go. - :arrow_down:1 - :star:1
* [neural-go](https://github.com/schuyler/neural-go) - A multilayer perceptron network implemented in Go, with training via backpropagation.
* [probab](https://github.com/ThePaw/probab) - Probability distribution functions. Bayesian inference. Written in pure Go. - :arrow_down:0 - :star:2
* [regommend](https://github.com/muesli/regommend) - Recommendation & collaborative filtering engine - :arrow_down:5 - :star:122
* [shield](https://github.com/eaigner/shield) - Bayesian text classifier with flexible tokenizers and storage backends for Go - :arrow_down:1 - :star:83


## Messaging

*Libraries that implement messaging systems*

* [Centrifugo](https://github.com/centrifugal/centrifugo) - Real-time messaging (Websockets or SockJS) server in Go. - :arrow_down:0 - :star:1222
* [dbus](https://github.com/godbus/dbus) - Native Go bindings for D-Bus. - :arrow_down:526 - :star:99
* [emitter](https://github.com/olebedev/emitter) - Emits events using Go way, with wildcard, predicates, cancellation possibilities and many other good wins. - :arrow_down:1 - :star:73
* [EventBus](https://github.com/asaskevich/EventBus) - The lightweight event bus with async compatibility. - :arrow_down:10 - :star:168
* [go-longpoll](https://github.com/ventu-io/go-longpoll) - PubSub with long polling. - :arrow_down:9 - :star:12
* [go-notify](https://github.com/TheCreeper/go-notify) - Native implementation of the freedesktop notification spec. - :arrow_down:3 - :star:13
* [go-nsq](https://github.com/nsqio/go-nsq) - the official Go package for NSQ - :arrow_down:267 - :star:642
* [gopush-cluster](https://github.com/Terry-Mao/gopush-cluster) - gopush-cluster is a go push server cluster.
* [gorush](https://github.com/appleboy/gorush) - A push notification server using [APNs2](https://github.com/sideshow/apns2) and google [GCM](https://github.com/google/go-gcm). - :arrow_down:0 - :star:277
* [guble](https://github.com/smancke/guble) - A messaging server using push notifications (Google Firebase Cloud Messaging, Apple Push Notification services, SMS) as well as websockets, a REST API, featuring distributed operation and message-persistence. - :arrow_down:0 - :star:34
* [machinery](https://github.com/RichardKnop/machinery) - An asynchronous task queue/job queue based on distributed message passing. - :arrow_down:0 - :star:701
* [mangos](https://github.com/go-mangos/mangos) - Pure go implementation of the Nanomsg ("Scalable Protocols") with transport interoperability. - :arrow_down:154 - :star:942
* [NATS Go Client](https://github.com/nats-io/nats) - A lightweight and high performance publish-subscribe and distributed queueing messaging system - this is the Go library. - :arrow_down:267 - :star:934
* [oplog](https://github.com/dailymotion/oplog) - A generic oplog/replication system for REST APIs - :arrow_down:0 - :star:74
* [pubsub](https://github.com/tuxychandru/pubsub) - A simple pubsub package for go. - :arrow_down:14 - :star:106
* [RapidMQ](https://github.com/sybrexsys/RapidMQ) - RapidMQ is a lightweight and reliable library for managing of the local messages queue
* [sarama](https://github.com/Shopify/sarama) - A Go library for Apache Kafka. - :arrow_down:625 - :star:1282
* [Uniqush-Push](https://github.com/uniqush/uniqush-push) - A redis backed unified push service for server-side notifications to mobile devices. - :arrow_down:0 - :star:862
* [zmq4](https://github.com/pebbe/zmq4) - A Go interface to ZeroMQ version 4. Also available for [version 3](https://github.com/pebbe/zmq3) and [version 2](https://github.com/pebbe/zmq2). - :arrow_down:321 - :star:415


## Miscellaneous

*These libraries were placed here because none of the other categories seemed to fit*

* [afero](https://github.com/spf13/afero) - A FileSystem Abstraction System for Go. - :arrow_down:1034 - :star:703
* [archiver](https://github.com/mholt/archiver) - Library and command for making and extracting .zip and .tar.gz archives - :arrow_down:92 - :star:135
* [autoflags](https://github.com/artyom/autoflags) - Go package to automatically define command line flags from struct fields. - :arrow_down:18 - :star:11
* [banner](https://github.com/dimiro1/banner) - Add beautiful banners into your Go applications. - :arrow_down:4 - :star:95
* [battery](https://github.com/distatus/battery) - A cross-platform, normalized battery information library. - :arrow_down:5 - :star:63
* [bitio](https://github.com/icza/bitio) - Highly optimized bit-level Reader and Writer for Go. - :arrow_down:2 - :star:6
* [browscap_go](https://github.com/digitalcrab/browscap_go) - GoLang Library for [Browser Capabilities Project](http://browscap.org/). - :arrow_down:0 - :star:17
* [conv](https://github.com/cstockton/go-conv) - Package conv provides fast and intuitive conversions across Go types. - :arrow_down:0 - :star:251
* [datacounter](https://github.com/miolini/datacounter) - Go counters for readers/writer/http.ResponseWriter. - :arrow_down:3 - :star:12
* [errors](https://github.com/pkg/errors) - A package that provides simple error handling primitives. - :arrow_down:1749 - :star:1032
* [go-chat-bot](https://github.com/go-chat-bot/bot) - IRC, Slack & Telegram bot written in Go. - :arrow_down:78 - :star:122
* [go-commons-pool](https://github.com/jolestar/go-commons-pool) - A generic object pool for Golang. - :arrow_down:1 - :star:287
* [go-multierror](https://github.com/hashicorp/go-multierror) - A Go (golang) package for representing a list of errors as a single error. - :arrow_down:1202 - :star:205
* [go-openapi](https://github.com/go-openapi) - A collection of packages to parse and utilize open-api schemas
* [go-shortid](https://github.com/ventu-io/go-shortid) - Distributed generation of super short, unique, non-sequential, URL friendly IDs. - :arrow_down:11 - :star:85
* [go.uuid](https://github.com/satori/go.uuid) - Implementation of Universally Unique Identifier (UUID). Supported both creation and parsing of UUIDs. - :arrow_down:1474 - :star:613
* [gopsutil](https://github.com/shirou/gopsutil) - A cross-platform library for retrieving process and system utilization(CPU, Memory, Disks, etc). - :arrow_down:4 - :star:1245
* [gosms](https://github.com/haxpax/gosms) - Your own local SMS gateway in Go that can be used to send SMS - :arrow_down:8 - :star:955
* [gountries](https://github.com/pariz/gountries) - A package that exposes country and subdivision data. - :arrow_down:2 - :star:103
* [hanu](https://github.com/sbstjn/hanu) - Framework for writing Slack bots. - :arrow_down:2 - :star:5
* [health](https://github.com/dimiro1/health) - A Easy to use, extensible health check library. - :arrow_down:9 - :star:193
* [indigo](https://github.com/osamingo/indigo) - A distributed unique ID generator of using Sonyflake and encoded by Base58. - :arrow_down:0 - :star:1
* [jobs](https://github.com/albrow/jobs) - A persistent and flexible background jobs library. - :arrow_down:2 - :star:353
* [margelet](https://github.com/zhulik/margelet) - A framework for building Telegram bots. - :arrow_down:5 - :star:35
* [notify](https://github.com/rjeczalik/notify) - File system event notification library with simple API, similar to os/signal. - :arrow_down:36 - :star:178
* [secdl](https://github.com/xor-gate/secdl) - Lighttpd ModSecDownload algorithm ported to go to secure download urls. - :arrow_down:0 - :star:1
* [stats](https://github.com/go-playground/stats) - Monitors Go MemStats + System stats such as Memory, Swap and CPU and sends via UDP anywhere you want for logging etc... - :arrow_down:0 - :star:36
* [werr](https://github.com/txgruppi/werr) - Error Wrapper creates an wrapper for the error type in Go which captures the File, Line and Stack of where it was called. - :arrow_down:0 - :star:5
* [xkg](https://github.com/go-xkg/xkg) - X Keyboard Grabber - :arrow_down:0 - :star:17
* [xstrings](https://github.com/huandu/xstrings) - A collection of useful string functions ported from other languages. - :arrow_down:12 - :star:342

## Natural Language Processing

*Libraries for working with human languages.*

* [dpar](https://github.com/danieldk/dpar/) - Transition-based statistical dependency parser.
* [go-eco](https://github.com/ThePaw/go-eco) - Similarity, dissimilarity and distance matrices; diversity, equitability and inequality measures; species richness estimators; coenocline models.
* [go-i18n](https://github.com/nicksnyder/go-i18n/) - A package and an accompanying tool to work with localized text.
* [go-mystem](https://github.com/dveselov/mystem) - CGo bindings to Yandex.Mystem - russian morphology analyzer. - :arrow_down:0 - :star:2
* [go-nlp](https://github.com/nuance/go-nlp) - Utilities for working with discrete probability distributions and other tools useful for doing NLP work.
* [go-stem](https://github.com/agonopol/go-stem) - Implementation of the porter stemming algorithm. - :arrow_down:17 - :star:39
* [go-unidecode](https://github.com/mozillazg/go-unidecode) - ASCII transliterations of Unicode text. - :arrow_down:2 - :star:5
* [go2vec](https://github.com/danieldk/go2vec) - Reader and utility functions for word2vec embeddings. - :arrow_down:1 - :star:12
* [gojieba](https://github.com/yanyiwu/gojieba) - This is a Go implementation of [jieba](https://github.com/fxsjy/jieba) which a Chinese word splitting algorithm. - :arrow_down:9 - :star:113
* [golibstemmer](https://github.com/rjohnsondev/golibstemmer) - Go bindings for the snowball libstemmer library including porter 2 - :arrow_down:0 - :star:11
* [gounidecode](https://github.com/fiam/gounidecode) - Unicode transliterator (also known as unidecode) for Go
* [icu](https://github.com/goodsign/icu) - Cgo binding for icu4c C library detection and conversion functions. Guaranteed compatibility with version 50.1. - :arrow_down:1 - :star:13
* [libtextcat](https://github.com/goodsign/libtextcat) - Cgo binding for libtextcat C library. Guaranteed compatibility with version 2.2. - :arrow_down:1 - :star:8
* [MMSEGO](https://github.com/awsong/MMSEGO) - This is a GO implementation of [MMSEG](http://technology.chtsai.org/mmseg/) which a Chinese word splitting algorithm. - :arrow_down:0 - :star:50
* [paicehusk](https://github.com/rookii/paicehusk) - Golang implementation of the Paice/Husk Stemming Algorithm - :arrow_down:6 - :star:15
* [porter](https://github.com/a2800276/porter) - This is a fairly straightforward port of Martin Porter's C implementation of the Porter stemming algorithm. - :arrow_down:1 - :star:2
* [porter2](https://github.com/zhenjl/porter2) - Really fast Porter 2 stemmer. - :arrow_down:4 - :star:26
* [segment](https://github.com/blevesearch/segment) - A Go library for performing Unicode Text Segmentation as described in [Unicode Standard Annex #29](http://www.unicode.org/reports/tr29/) - :arrow_down:7 - :star:18
* [sentences](https://github.com/neurosnap/sentences) - A sentence tokenizer:  converts text into a list of sentences. - :arrow_down:1 - :star:145
* [snowball](https://github.com/goodsign/snowball) - Snowball stemmer port (cgo wrapper) for Go. Provides word stem extraction functionality [Snowball native](http://snowball.tartarus.org/). - :arrow_down:1 - :star:14
* [stemmer](https://github.com/dchest/stemmer) - Stemmer packages for Go programming language. Includes English and German stemmers. - :arrow_down:3 - :star:31
* [textcat](https://github.com/pebbe/textcat) - A Go package for n-gram based text categorization, with support for utf-8 and raw text - :arrow_down:6 - :star:41

## Networking

*Libraries for working with various layers of the network*

* [arp](https://github.com/mdlayher/arp) - Package arp implements the ARP protocol, as described in RFC 826. - :arrow_down:6 - :star:49
* [buffstreams](https://github.com/stabbycutyou/buffstreams) - Streaming protocolbuffer data over TCP made easy
* [canopus](https://github.com/zubairhamed/canopus) - CoAP Client/Server implementation (RFC 7252) - :arrow_down:5 - :star:38
* [dhcp6](https://github.com/mdlayher/dhcp6) - Package dhcp6 implements a DHCPv6 server, as described in RFC 3315. - :arrow_down:4 - :star:15
* [dns](https://github.com/miekg/dns) - Go library for working with DNS
* [ether](https://github.com/songgao/ether) - A cross-platform Go package for sending and receiving ethernet frames. - :arrow_down:0 - :star:36
* [ethernet](https://github.com/mdlayher/ethernet) - Package ethernet implements marshaling and unmarshaling of IEEE 802.3 Ethernet II frames and IEEE 802.1Q VLAN tags. - :arrow_down:13 - :star:15
* [fasthttp](https://github.com/valyala/fasthttp) - Package fasthttp is a fast HTTP implementation for Go, up to 10 times faster than net/http - :arrow_down:432 - :star:3116
* [ftp](https://github.com/jlaffaye/ftp) - Package ftp implements a FTP client as described in [RFC 959](http://tools.ietf.org/html/rfc959). - :arrow_down:32 - :star:143
* [go-getter](https://github.com/hashicorp/go-getter) - A Go library for downloading files or directories from various sources using a URL. - :arrow_down:228 - :star:277
* [go-stun](https://github.com/ccding/go-stun) - A go implementation of the STUN client (RFC 3489 and RFC 5389). - :arrow_down:0 - :star:97
* [gobgp](https://github.com/osrg/gobgp) - BGP implemented in the Go Programming Language.
* [golibwireshark](https://github.com/sunwxg/golibwireshark) - Package golibwireshark use libwireshark library to decode pcap file and analyse dissection data. - :arrow_down:0 - :star:4
* [gopacket](https://github.com/google/gopacket) - A Go library for packet processing with libpcap bindings - :arrow_down:672 - :star:747
* [gopcap](https://github.com/akrennmair/gopcap) - A Go wrapper for libpcap - :arrow_down:86 - :star:226
* [goshark](https://github.com/sunwxg/goshark) - Package goshark use tshark to decode IP packet and create data struct to analyse packet. - :arrow_down:3 - :star:1
* [gosnmp](https://github.com/soniah/gosnmp) - Native Go library for performing SNMP actions - :arrow_down:63 - :star:121
* [gotcp](https://github.com/gansidui/gotcp) - A Go package for quickly writing tcp applications - :arrow_down:29 - :star:201
* [grab](https://github.com/cavaliercoder/grab) - Go package for managing file downloads - :arrow_down:6 - :star:56
* [graval](https://github.com/koofr/graval) - An experimental FTP server framework. - :arrow_down:6 - :star:13
* [kcp-go](https://github.com/xtaci/kcp-go) - KCP - A Fast and Reliable ARQ Protocol. - :arrow_down:37 - :star:231
* [kcptun](https://github.com/xtaci/kcptun) - An extremely simple & fast udp tunnel based on KCP protocol
* [lhttp](https://github.com/fanux/lhttp) - A powerful websocket framework, build your IM server more easily. - :arrow_down:1 - :star:232
* [linkio](https://github.com/ian-kent/linkio) - Network link speed simulation for Reader/Writer interfaces - :arrow_down:6 - :star:17
* [llb](https://github.com/kirillDanshin/llb) - It's a very simple but quick backend for proxy servers. Can be useful for fast redirection to predefined domain with zero memory allocation and fast response. - :arrow_down:0 - :star:1
* [mdns](https://github.com/hashicorp/mdns) - Simple mDNS (Multicast DNS) client/server library in Golang - :arrow_down:22 - :star:271
* [mqttPaho](https://eclipse.org/paho/clients/golang/) - The Paho Go Client provides an MQTT client library for connection to MQTT brokers via TCP, TLS or WebSockets.
* [portproxy](https://github.com/aybabtme/portproxy) - Simple TCP proxy which adds CORS support to API's which don't support it.
* [raw](https://github.com/mdlayher/raw) - Package raw enables reading and writing data at the device driver level for a network interface. - :arrow_down:8 - :star:34
* [sftp](https://github.com/pkg/sftp) - Package sftp implements the SSH File Transfer Protocol as described in https://filezilla-project.org/specs/draft-ietf-secsh-filexfer-02.txt. - :arrow_down:204 - :star:285
* [sslb](https://github.com/eduardonunesp/sslb) - It's a Super Simples Load Balancer, just a little project to achieve some kind of performance. - :arrow_down:0 - :star:67
* [tcp_server](https://github.com/firstrow/tcp_server) - A Go library for building tcp servers faster. - :arrow_down:7 - :star:54
* [utp](https://github.com/anacrolix/utp) - Go uTP micro transport protocol implementation. - :arrow_down:29 - :star:58
* [winrm](https://github.com/masterzen/winrm) - A Go WinRM client to remotely execute commands on Windows machines - :arrow_down:4 - :star:90

## OpenGL

*Libraries for using OpenGL in Go.*

* [gl](https://github.com/go-gl/gl) - Go bindings for OpenGL (generated via glow).
* [glfw](https://github.com/go-gl/glfw) - Go bindings for GLFW 3.
* [goxjs/gl](https://github.com/goxjs/gl) - Go cross-platform OpenGL bindings (OS X, Linux, Windows, browsers, iOS, Android). - :arrow_down:35 - :star:69
* [goxjs/glfw](https://github.com/goxjs/glfw) - Go cross-platform glfw library for creating an OpenGL context and receiving events. - :arrow_down:37 - :star:29
* [mathgl](https://github.com/go-gl/mathgl) - Pure Go math package specialized for 3D math, with inspiration from GLM.


## ORM

*Libraries that implement Object-Relational Mapping or datamapping techniques.*

* [beego orm](https://github.com/astaxie/beego/tree/master/orm) - A powerful orm framework for go. Support: pq/mysql/sqlite3.
* [go-store](https://github.com/gosuri/go-store) - A simple and fast Redis backed key-value store library for Go.
* [gomodel](https://github.com/cosiner/gomodel) - A lightweight, fast, orm-like library helps interactive with database. - :arrow_down:4 - :star:47
* [GORM](https://github.com/jinzhu/gorm) - The fantastic ORM library for Golang, aims to be developer friendly. - :arrow_down:1645 - :star:4358
* [gorp](https://github.com/go-gorp/gorp) - Go Relational Persistence, ORM-ish library for Go. - :arrow_down:228 - :star:2211
* [QBS](https://github.com/coocood/qbs) - Stands for Query By Struct. A Go ORM. - :arrow_down:63 - :star:417
* [reform](https://github.com/go-reform/reform) - A better ORM for Go, based on non-empty interfaces and code generation. - :arrow_down:0 - :star:384
* [SQLBoiler](https://github.com/vattle/sqlboiler) - An ORM generator. Generate a featureful and blazing-fast ORM tailored to your database schema. - :arrow_down:0 - :star:174
* [Storm](https://github.com/asdine/storm) - Simple and powerful ORM for BoltDB. - :arrow_down:42 - :star:255
* [upper.io/db](https://github.com/upper/db) - Single interface for interacting with different data sources through the use of adapters that wrap mature database drivers. - :arrow_down:0 - :star:474
* [Xorm](https://github.com/go-xorm/xorm) - Simple and powerful ORM for Go. - :arrow_down:915 - :star:1369
* [Zoom](https://github.com/albrow/zoom) - A blazing-fast datastore and querying engine built on Redis. - :arrow_down:17 - :star:142

## Package Management

*Libraries for package and dependency management.*

* [gigo](https://github.com/LyricalSecurity/gigo) - PIP-like dependency tool for golang, with support for private repositories and hashes. - :arrow_down:0 - :star:187
* [glide](https://github.com/Masterminds/glide) - Manage your golang vendor and vendored packages with ease. Inspired by tools like Maven, Bundler, and Pip. - :arrow_down:0 - :star:2701
* [godep](https://github.com/tools/godep) - dependency tool for go, godep helps build packages reproducibly by fixing their dependencies. - :arrow_down:0 - :star:3930
* [gom](https://github.com/mattn/gom) - Go Manager - bundle for go. - :arrow_down:0 - :star:1152
* [goop](https://github.com/nitrous-io/goop) - A simple dependency manager for Go (golang), inspired by Bundler. - :arrow_down:0 - :star:765
* [gopm](https://github.com/gpmgo/gopm) - Go Package Manager - :arrow_down:0 - :star:1140
* [govendor](https://github.com/kardianos/govendor) - Go Package Manager. Go vendor tool that works with the standard vendor file. - :arrow_down:0 - :star:1081
* [gpm](https://github.com/pote/gpm) - Barebones dependency manager for Go.
* [gvt](https://github.com/FiloSottile/gvt) - `gvt` is a simple vendoring tool made for Go native vendoring (aka GO15VENDOREXPERIMENT), based on gb-vendor. - :arrow_down:0 - :star:511
* [johnny-deps](https://github.com/VividCortex/johnny-deps) - Minimal dependency version using Git
* [nut](https://github.com/jingweno/nut) - Vendor Go dependencies - :arrow_down:0 - :star:244
* [VenGO](https://github.com/DamnWidget/VenGO) - create and manage exportable isolated go virtual environments - :arrow_down:0 - :star:89




## Query Language

* [graphql](https://github.com/tmc/graphql) - graphql parser + utilities. - :arrow_down:25 - :star:39
* [graphql](https://github.com/sevki/graphql) - GraphQL implementation in go. - :arrow_down:0 - :star:31
* [graphql-go](https://github.com/graphql-go/graphql) - An implementation of GraphQL for Go. - :arrow_down:129 - :star:549
* [jsonql](https://github.com/elgs/jsonql) - JSON query expression library in Golang. - :arrow_down:1 - :star:63


## Resource Embedding

* [esc](https://github.com/mjibson/esc) - Embeds files into Go programs and provides http.FileSystem interfaces to them. - :arrow_down:0 - :star:153
* [fileb0x](https://github.com/UnnoTed/fileb0x) - Simple tool to embed files in go with focus on "customization" and ease to use. - :arrow_down:0 - :star:81
* [go-bindata](https://github.com/jteeuwen/go-bindata) - Package that converts any file into managable Go source code. - :arrow_down:110 - :star:2158
* [go-embed](https://github.com/pyros2097/go-embed) - Generates go code to embed resource files into your library or executable - :arrow_down:0 - :star:3
* [go-resources](https://github.com/omeid/go-resources) - Unfancy resources embedding with Go. - :arrow_down:3 - :star:107
* [go.rice](https://github.com/GeertJohan/go.rice) - go.rice is a Go package that makes working with resources such as html,js,css,images and templates very easy. - :arrow_down:361 - :star:788
* [statics](https://github.com/go-playground/statics) - Embeds static resources into go files for single binary compilation + works with http.FileSystem + symlinks. - :arrow_down:0 - :star:34
* [vfsgen](https://github.com/shurcooL/vfsgen) - Generates a vfsdata.go file that statically implements the given virtual filesystem. - :arrow_down:1 - :star:97


## Science and Data Analysis

*Libraries for scientific computing and data analyzing.*

* [blas](https://github.com/ziutek/blas) - Implementation of BLAS (Basic Linear Algebra Subprograms) - :arrow_down:11 - :star:92
* [chart](https://github.com/vdobler/chart) - Simple Chart Plotting library for Go. Supports many graphs types. - :arrow_down:89 - :star:353
* [evaler](https://github.com/soniah/evaler) - A simple floating point arithmetic expression evaluator - :arrow_down:2 - :star:24
* [ewma](https://github.com/VividCortex/ewma) - Exponentially-weighted moving averages - :arrow_down:32 - :star:159
* [geom](https://github.com/skelterjohn/geom) - 2D geometry for golang - :arrow_down:92 - :star:32
* [go-dsp](https://github.com/mjibson/go-dsp) - Digital Signal Processing for Go
* [go-fn](https://github.com/ematvey/go-fn) - Mathematical functions written in Go language, that are not covered by math pkg
* [go-gt](https://github.com/ThePaw/go-gt) - Graph theory algorithms written in "Go" language - :arrow_down:0 - :star:1
* [go.matrix](https://github.com/skelterjohn/go.matrix) - linear algebra for go (has been stalled) - :arrow_down:102 - :star:259
* [gocomplex](https://github.com/varver/gocomplex) - A complex number library for the Go programming language.
* [gofrac](https://github.com/anschelsc/gofrac) - A (goinstallable) fractions library for go with support for basic arithmetic. - :arrow_down:0 - :star:6
* [gohistogram](https://github.com/VividCortex/gohistogram) - Approximate histograms for data streams - :arrow_down:8 - :star:78
* [gonum/mat64](https://github.com/gonum/matrix) - The general purpose package for matrix computation. Package mat64 provides basic linear algebra operations for float64 matrices.
* [gonum/plot](https://github.com/gonum/plot) - gonum/plot provides an API for building and drawing plots in Go. - :arrow_down:121 - :star:343
* [goraph](https://github.com/gyuho/goraph) - A pure Go graph theory library(data structure, algorith visualization) - :arrow_down:1 - :star:246
* [gostat](https://github.com/ematvey/gostat) - A statistics library for the go language - :arrow_down:6 - :star:11
* [mudlark-go](https://github.com/pwil3058/mudlark-go-pkgs) - A collection of packages providing (hopefully) useful code for use in software using Google's Go programming language.
* [ode](https://github.com/ChristopherRabotin/ode) - An ordinary differential equation (ODE) solver which supports extended states and channel-based iteration stop conditions. - :arrow_down:0 - :star:1
* [pagerank](https://github.com/alixaxel/pagerank) - Weighted PageRank algorithm implemented in Go - :arrow_down:2 - :star:17
* [PiHex](https://github.com/claygod/PiHex) - Implementation of the "Bailey-Borwein-Plouffe" algorithm for the hexadecimal number Pi - :arrow_down:0 - :star:3
* [stats](https://github.com/montanaflynn/stats) - A statistics package with common functions missing from the Golang standard library. - :arrow_down:88 - :star:626
* [streamtools](https://github.com/nytlabs/streamtools) - general purpose, graphical tool for dealing with streams of data.
* [vectormath](https://github.com/spate/vectormath) - Vectormath for Go, an adaptation of the scalar C functions from Sony's Vector Math library, as found in the Bullet-2.79 source code. (currently inactive) - :arrow_down:6 - :star:53


## Security

*Libraries that are used to help make your application more secure.*

* [acmetool](https://github.com/hlandau/acme) — ACME (Let's Encrypt) client tool with automatic renewal.
* [BadActor](https://github.com/jaredfolkins/badactor) - An in-memory, application-driven jailer built in the spirit of fail2ban - :arrow_down:2 - :star:178
* [go-yara](https://github.com/hillu/go-yara) - Go Bindings for [YARA](https://github.com/plusvic/yara), the "pattern matching swiss knife for malware researchers (and everyone else)" - :arrow_down:1 - :star:33
* [lego](https://github.com/xenolf/lego) - Pure Go ACME client library and CLI tool (for use with Let's Encrypt) - :arrow_down:0 - :star:1486
* [passlib](https://github.com/hlandau/passlib) - Futureproof password hashing library. - :arrow_down:0 - :star:109
* [simple-scrypt](https://github.com/elithrar/simple-scrypt) - an scrypt package with a simple, obvious API and automatic cost calibration built-in. - :arrow_down:10 - :star:72

## Serialization

*Libraries and tools for binary serialization*

* [asn1](https://github.com/PromonLogicalis/asn1) - Asn.1 BER and DER encoding library for golang - :arrow_down:1 - :star:5
* [colfer](https://github.com/pascaldekloe/colfer) - Code generation for the Colfer binary format - :arrow_down:1 - :star:42
* [go-capnproto](https://github.com/glycerine/go-capnproto) - Cap'n Proto library and parser for go - :arrow_down:99 - :star:249
  * [bambam](https://github.com/glycerine/bambam) - generator for Cap'n Proto schemas from go. - :arrow_down:0 - :star:54
* [go-codec](https://github.com/ugorji/go) - High Performance, feature-Rich, idiomatic encode, decode and rpc library for msgpack, cbor and json, with runtime-based OR code-generation support
* [gogoprotobuf](https://github.com/gogo/protobuf) - Protocol Buffers for Go with Gadgets
* [goprotobuf](https://github.com/golang/protobuf) - Go support, in the form of a library and protocol compiler plugin, for Google's protocol buffers.
* [mapstructure](https://github.com/mitchellh/mapstructure) - Go library for decoding generic map values into native Go structures. - :arrow_down:2365 - :star:676
* [php_session_decoder](https://github.com/yvasiyarov/php_session_decoder) - GoLang library for working with PHP session format and PHP Serialize/Unserialize functions - :arrow_down:0 - :star:56
* [structomap](https://github.com/tuvistavie/structomap) - Library to easily and dynamically generate maps from static structures. - :arrow_down:0 - :star:39


## Server Applications

* [algernon](https://github.com/xyproto/algernon) - HTTP/2 web server with built-in support for Lua, Markdown, GCSS and Amber. - :arrow_down:0 - :star:268
* [Caddy](https://github.com/mholt/caddy) - Caddy is an alternative, HTTP/2 web server that's easy to configure and use. - :arrow_down:581 - :star:8166
* [consul](https://www.consul.io/) - Consul is a tool for service discovery, monitoring and configuration.
* [devd](https://github.com/cortesi/devd) - A local webserver for developers - :arrow_down:2 - :star:2181
* [etcd](https://github.com/coreos/etcd) - A highly-available key value store for shared configuration and service discovery. - :arrow_down:0 - :star:11011
* [minio](https://github.com/minio/minio) - Minio is a distributed object storage server. - :arrow_down:0 - :star:4239
* [nsq](http://nsq.io/) - A realtime distributed messaging platform
* [yakvs](https://github.com/sci4me/yakvs) - A small, networked, in-memory key-value store. - :arrow_down:0 - :star:8


## Template Engines

*Libraries and tools for templating and lexing.*

* [ace](https://github.com/yosssi/ace) - Ace is an HTML template engine for Go, inspired by Slim and Jade. Ace is a refinement of Gold. - :arrow_down:326 - :star:507
* [amber](https://github.com/eknkc/amber) - Amber is an elegant templating engine for Go Programming Language It is inspired from HAML and Jade. - :arrow_down:361 - :star:644
* [damsel](https://github.com/dskinner/damsel) - Markup language featuring html outlining via css-selectors, extensible via pkg html/template and others. - :arrow_down:0 - :star:16
* [ego](https://github.com/benbjohnson/ego) - A lightweight templating language that lets you write templates in Go. Templates are translated into Go and compiled. - :arrow_down:1 - :star:274
* [fasttemplate](https://github.com/valyala/fasttemplate) - Simple and fast template engine. Substitutes template placeholders up to 10x faster than [text/template](http://golang.org/pkg/text/template/). - :arrow_down:63 - :star:93
* [gofpdf](https://github.com/jung-kurt/gofpdf) - A PDF document generator with high level support for text, drawing and images. - :arrow_down:118 - :star:335
* [jet](https://github.com/CloudyKit/jet) - Jet template engine - :arrow_down:14 - :star:310
* [kasia.go](https://github.com/ziutek/kasia.go) - Templating system for HTML and other text documents - go implementation. - :arrow_down:3 - :star:67
* [mustache](https://github.com/hoisie/mustache) - A Go implementation of the Mustache template language. - :arrow_down:114 - :star:803
* [pongo2](https://github.com/flosch/pongo2) - A Django-like template-engine for Go. - :arrow_down:179 - :star:795
* [quicktemplate](https://github.com/valyala/quicktemplate) - Fast, powerful, yet easy to use template engine. Converts templates into Go code and then compiles it. - :arrow_down:7 - :star:533
* [raymond](https://github.com/aymerick/raymond) - A complete handlebars implementation in Go. - :arrow_down:32 - :star:109
* [Razor](https://github.com/sipin/gorazor) - Razor view engine for Golang. - :arrow_down:0 - :star:537
* [Soy](https://github.com/robfig/soy) - Closure templates (aka Soy templates) for Go, following the [official spec](https://developers.google.com/closure/templates/) - :arrow_down:5 - :star:116


## Testing

*Libraries for testing codebases and generating test data.*

* Testing Frameworks
    * [assert](https://github.com/go-playground/assert) - Basic Assertion Library used along side native go testing, with building blocks for custom assertions - :arrow_down:0 - :star:6
    * [badio](https://github.com/cavaliercoder/badio) - Extensions to Go's `testing/iotest` package - :arrow_down:0 - :star:2
    * [baloo](https://github.com/h2non/baloo) - Expressive and versatile end-to-end HTTP API testing made easy. - :arrow_down:0 - :star:222
    * [bro](https://github.com/marioidival/bro) - Watch files in directory and run tests for them - :arrow_down:0 - :star:11
    * [dsunit](https://github.com/viant/dsunit) - Datastore testing for SQL, NoSQL, structured files. - :arrow_down:1 - :star:2
    * [frisby](https://github.com/verdverm/frisby) - a REST API testing framework - :arrow_down:4 - :star:159
    * [ginkgo](http://onsi.github.io/ginkgo/) - BDD Testing Framework for Go
    * [go-carpet](https://github.com/msoap/go-carpet) - Tool for viewing test coverage in terminal - :arrow_down:0 - :star:147
    * [go-mutesting](https://github.com/zimmski/go-mutesting) - Mutation testing for Go source code - :arrow_down:5 - :star:70
    * [go-vcr](https://github.com/dnaeon/go-vcr) - Record and replay your HTTP interactions for fast, deterministic and accurate tests
    * [goblin](https://github.com/franela/goblin) - Mocha like testing framework fo Go - :arrow_down:0 - :star:306
    * [gocheck](http://labix.org/gocheck) - A more advanced testing framework alternative to gotest.
    * [GoConvey](https://github.com/smartystreets/goconvey/) - BDD-style framework with web UI and live reload
    * [godog](https://github.com/DATA-DOG/godog) - Cucumber or Behat like BDD framework for Go. - :arrow_down:9 - :star:94
    * [gofight](https://github.com/appleboy/gofight) - API Handler Testing for Golang Router framework. - :arrow_down:0 - :star:50
    * [gomega](http://onsi.github.io/gomega/) - Rspec like matcher/assertion library.
    * [GoSpec](https://github.com/orfjackal/gospec) - BDD-style testing framework for the Go programming language.
    * [gospecify](https://github.com/stesla/gospecify) - This provides a BDD syntax for testing your Go code. It should be familiar to anybody who has used libraries such as rspec.
    * [gosuite](https://github.com/pavlo/gosuite) - Brings lightweight test suites with setup/teardown facilities to `testing` by leveraging Go1.7's Subtests - :arrow_down:0 - :star:0
    * [Hamcrest](https://github.com/rdrdr/hamcrest) - fluent framework for declarative Matcher objects that, when applied to input values, produce self-describing results. - :arrow_down:0 - :star:23
    * [httpexpect](https://github.com/gavv/httpexpect) - Concise, declarative, and easy to use end-to-end HTTP and REST API testing - :arrow_down:23 - :star:580
    * [restit](https://github.com/yookoala/restit) - A Go micro framework to help writing RESTful API integration test.
    * [testfixtures](https://github.com/go-testfixtures/testfixtures) - A helper for Rails' like test fixtures to test database applications. - :arrow_down:0 - :star:67
    * [Testify](https://github.com/stretchr/testify) - A sacred extension to the standard go testing package. - :arrow_down:0 - :star:2304

* Mock
    * [counterfeiter](https://github.com/maxbrunsfeld/counterfeiter) - Tool for generating self-contained mock objects - :arrow_down:0 - :star:100
    * [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock) - Mock SQL driver for testing database interactions - :arrow_down:11 - :star:273
    * [go-txdb](https://github.com/DATA-DOG/go-txdb) - Single transaction based database driver mainly for testing purposes. - :arrow_down:0 - :star:9
    * [gock](https://github.com/h2non/gock) - Versatile HTTP mocking made easy. - :arrow_down:1 - :star:227
    * [gomock](https://github.com/golang/mock) - Mocking framework for the Go programming language.
    * [govcr](https://github.com/seborama/govcr) -  HTTP mock for Golang: record and replay HTTP interactions for offline testing - :arrow_down:3 - :star:8
    * [mockhttp](https://github.com/tv42/mockhttp) - Mock object for Go http.ResponseWriter - :arrow_down:0 - :star:19

* Fuzzing and delta-debugging/reducing/shrinking
    * [go-fuzz](https://github.com/dvyukov/go-fuzz) - A randomized testing system
    * [gofuzz](https://github.com/google/gofuzz) - A library for populating go objects with random values - :arrow_down:309 - :star:244
    * [Tavor](https://github.com/zimmski/tavor) - A generic fuzzing and delta-debugging framework - :arrow_down:7 - :star:148

## Text Processing

*Libraries for parsing and manipulating texts.*

* Specific Formats
    * [allot](https://github.com/sbstjn/allot) - Placeholder and wildcard text parsing for CLI tools and bots - :arrow_down:0 - :star:2
    * [bbConvert](https://github.com/CalebQ42/bbConvert) - Converts bbCode to HTML that allows you to add support for custom bbCode tags - :arrow_down:0 - :star:0
    * [blackfriday](https://github.com/russross/blackfriday) - Markdown processor in Go - :arrow_down:1944 - :star:1984
        * [github_flavored_markdown](https://godoc.org/github.com/shurcooL/github_flavored_markdown) - GitHub Flavored Markdown renderer with fenced code block highlighting, clickable header anchor links.
    * [bluemonday](https://github.com/microcosm-cc/bluemonday) - HTML Sanitizer - :arrow_down:262 - :star:466
    * [editorconfig-core-go](https://github.com/editorconfig/editorconfig-core-go) - Editorconfig file parser and manipulator for Go
    * [enca](https://github.com/endeveit/enca) - Minimal cgo bindings for [libenca](http://cihar.com/software/enca/). - :arrow_down:0 - :star:2
    * [genex](https://github.com/alixaxel/genex) - Count and expand Regular Expressions into all matching Strings - :arrow_down:0 - :star:36
    * [go-humanize](https://github.com/dustin/go-humanize) - Formatters for time, numbers, and memory size to human readable format. - :arrow_down:1081 - :star:752
    * [go-nmea](https://github.com/adrianmo/go-nmea) - NMEA parser library for the Go language. - :arrow_down:0 - :star:17
    * [go-pkg-rss](https://github.com/jteeuwen/go-pkg-rss) - This package reads RSS and Atom feeds and provides a caching mechanism that adheres to the feed specs. - :arrow_down:89 - :star:280
    * [go-pkg-xmlx](https://github.com/jteeuwen/go-pkg-xmlx) - Extension to the standard Go XML package. Maintains a node tree that allows forward/backwards browsing and exposes some simple single/multi-node search functions. - :arrow_down:75 - :star:112
    * [go-runewidth](https://github.com/mattn/go-runewidth) - Functions to get fixed width of the character or string. - :arrow_down:220 - :star:57
    * [go-slugify](https://github.com/mozillazg/go-slugify) - Make pretty slug with multiple languages support. - :arrow_down:1 - :star:5
    * [gofeed](https://github.com/mmcdole/gofeed) - Parse RSS and Atom feeds in Go - :arrow_down:6 - :star:486
    * [gographviz](https://github.com/awalterschulze/gographviz) - Parses the Graphviz DOT language. - :arrow_down:54 - :star:55
    * [gommon/bytes](https://github.com/labstack/gommon/tree/master/bytes) - Format bytes to string.
    * [gonameparts](https://github.com/polera/gonameparts) - Parses human names into individual name parts - :arrow_down:0 - :star:20
    * [GoQuery](https://github.com/PuerkitoBio/goquery) - GoQuery brings a syntax and a set of features similar to jQuery to the Go language. - :arrow_down:1581 - :star:3162
    * [goregen](https://github.com/zach-klippenstein/goregen) - A library for generating random strings from regular expressions. - :arrow_down:32 - :star:20
    * [gotext](https://github.com/leonelquinteros/gotext) - GNU gettext utilities for Go. - :arrow_down:1 - :star:105
    * [guesslanguage](https://github.com/endeveit/guesslanguage) - Functions to determine the natural language of a unicode text. - :arrow_down:2 - :star:21
    * [inject](https://github.com/facebookgo/inject) - Package inject provides a reflect based injector. - :arrow_down:61 - :star:500
    * [mxj](https://github.com/clbanning/mxj) - Encode / decode XML as JSON or map[string]interface{}; extract values with dot-notation paths and wildcards. Replaces x2j and j2x packages. - :arrow_down:80 - :star:132
    * [sh](https://github.com/mvdan/sh) - A shell parser and formatter
    * [slug](https://github.com/gosimple/slug) - URL-friendly slugify with multiple languages support. - :arrow_down:88 - :star:80
    * [Slugify](https://github.com/avelino/slugify) - A Go slugify application that handles string. - :arrow_down:3 - :star:11
    * [toml](https://github.com/BurntSushi/toml) - TOML configuration format (encoder/decoder with reflection). - :arrow_down:2572 - :star:1016
* Utility
    * [gotabulate](https://github.com/bndr/gotabulate) - Easily pretty-print your tabular data with Go. - :arrow_down:16 - :star:127
    * [kace](https://github.com/codemodus/kace) - Common case conversions covering common initialisms. - :arrow_down:2 - :star:1
    * [parseargs-go](https://github.com/nproc/parseargs-go) - A string argument parser that understands quotes and backslashes - :arrow_down:0 - :star:3
    * [parth](https://github.com/codemodus/parth) - URL path segmentation parsing. - :arrow_down:3 - :star:8
    * [xurls](https://github.com/mvdan/xurls) - Extract urls from text - :arrow_down:51 - :star:202


## Third-party APIs

*Libraries for accessing third party APIs.*

* [amazon-product-advertising-api](https://github.com/ngs/go-amazon-product-advertising-api) - Go Client Library for [Amazon Product Advertising API](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html)
* [anaconda](https://github.com/ChimeraCoder/anaconda) - A Go client library for the Twitter 1.1 API - :arrow_down:287 - :star:581
* [aws-sdk-go](https://github.com/aws/aws-sdk-go) - The official AWS SDK for the Go programming language. - :arrow_down:0 - :star:2752
* [brewerydb](https://github.com/naegelejd/brewerydb) - Go library for accessing the BreweryDB API. - :arrow_down:1 - :star:10
* [cachet](https://github.com/andygrunwald/cachet) - Go client library for [Cachet (open source status page system)](https://cachethq.io/) - :arrow_down:0 - :star:27
* [circleci](https://github.com/jszwedko/go-circleci) - A Go client library for interacting with CircleCI's API - :arrow_down:1 - :star:9
* [clarifai](https://github.com/samuelcouch/clarifai) - A Go client library for interfacing with the Clarifai API.
* [discordgo](https://github.com/bwmarrin/discordgo) -  Go bindings for the Discord Chat API - :arrow_down:112 - :star:150
* [facebook](https://github.com/huandu/facebook) - Go Library that supports the Facebook Graph API - :arrow_down:50 - :star:340
* [gads](https://github.com/emiddleton/gads) - Google Adwords Unofficial API - :arrow_down:20 - :star:20
* [gami](https://github.com/bit4bit/gami) - Go library for Asterisk Manager Interface. - :arrow_down:4 - :star:17
* [gcm](https://github.com/Aorioli/gcm) - Go library for Google Cloud Messaging - :arrow_down:0 - :star:29
* [geo-golang](https://github.com/codingsince1985/geo-golang) - Go Library to access [Google Maps](https://developers.google.com/maps/documentation/geocoding/intro), [MapQuest](http://open.mapquestapi.com/geocoding/), [Nominatim](http://open.mapquestapi.com/nominatim/), [OpenCage](http://geocoder.opencagedata.com/api.html), [HERE](https://developer.here.com/rest-apis/documentation/geocoder), [Bing](https://msdn.microsoft.com/en-us/library/ff701715.aspx), [Mapbox](https://www.mapbox.com/developers/api/geocoding/), and [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Nominatim) geocoding / reverse geocoding APIs. - :arrow_down:38 - :star:136
* [ghost](https://github.com/neuegram/ghost) - Go Library for accessing the Snapchat API. - :arrow_down:4 - :star:15
* [github](https://github.com/google/go-github) - Go library for accessing the GitHub API.
* [go-imgur](https://github.com/koffeinsource/go-imgur) - Go client library for [imgur](https://imgur.com) - :arrow_down:5 - :star:2
* [go-jira](https://github.com/andygrunwald/go-jira) - Go client library for [Atlassian JIRA](https://www.atlassian.com/software/jira) - :arrow_down:16 - :star:48
* [go-marathon](https://github.com/gambol99/go-marathon) - A Go library for interacting with Mesosphere's Marathon PAAS. - :arrow_down:180 - :star:106
* [go-trending](https://github.com/andygrunwald/go-trending) - Go library for accessing [trending repositories](https://github.com/trending) and [developers](https://github.com/trending/developers) at Github. - :arrow_down:2 - :star:74
* [go-twitter](https://github.com/dghubble/go-twitter) - Go client library for the Twitter v1.1 APIs.
* [go-xkcd](https://github.com/nishanths/go-xkcd) - Go client for the xkcd API. - :arrow_down:0 - :star:17
* [goamz](https://github.com/mitchellh/goamz) - Popular fork of [goamz](https://launchpad.net/goamz) which adds some missing API calls to certain packages.
* [golyrics](https://github.com/mamal72/golyrics) - Golyrics is a Go library to fetch music lyrics data from the Wikia website.
* [GoMusicBrainz](https://github.com/michiwend/gomusicbrainz) - a Go MusicBrainz WS2 client library. - :arrow_down:6 - :star:19
* [google](https://github.com/google/google-api-go-client) - Auto-generated Google APIs for Go.
* [google-analytics](https://github.com/chonthu/go-google-analytics) - A simple wrapper for easy google analytics reporting. - :arrow_down:1 - :star:5
* [google-cloud](https://github.com/GoogleCloudPlatform/gcloud-golang) - Google Cloud APIs Go Client Library. - :arrow_down:0 - :star:452
* [google-email-audit-api](https://github.com/ngs/go-google-email-audit-api) - Go client library for [Google G Suite Email Audit API](https://developers.google.com/admin-sdk/email-audit/).
* [gostorm](https://github.com/jsgilmore/gostorm) - GoStorm is a Go library that implements the communications protocol required to write Storm spouts and Bolts in Go that communicate with the Storm shells. - :arrow_down:5 - :star:85
* [hipchat](https://github.com/andybons/hipchat) - This project implements a golang client library for the Hipchat API. - :arrow_down:73 - :star:99
* [hipchat (xmpp)](https://github.com/daneharrigan/hipchat) - A golang package to communicate with HipChat over XMPP. - :arrow_down:27 - :star:95
* [Medium](https://github.com/Medium/medium-sdk-go) - A Golang SDK for Medium's OAuth2 API. - :arrow_down:0 - :star:51
* [megos](https://github.com/andygrunwald/megos) - A client library for accessing an [Apache Mesos](http://mesos.apache.org/) cluster - :arrow_down:3 - :star:39
* [micha](https://github.com/onrik/micha) - Go Library for Telegram bot api. - :arrow_down:1 - :star:0
* [minio-go](https://github.com/minio/minio-go) - Minio Go Library for Amazon S3 compatible cloud storage. - :arrow_down:41 - :star:193
* [mixpanel](https://github.com/dukex/mixpanel) - Mixpanel is a library for tracking events and sending Mixpanel profile updates to Mixpanel from your go applications. - :arrow_down:2 - :star:14
* [paypal](https://github.com/logpacker/paypalsdk) - Wrapper for PayPal payment API - :arrow_down:0 - :star:106
* [playlyfe](https://github.com/playlyfe/playlyfe-go-sdk) - The Playlyfe Rest API Go SDK - :arrow_down:0 - :star:0
* [pushover](https://github.com/gregdel/pushover) - Go wrapper for the Pushover API. - :arrow_down:5 - :star:13
* [rrdaclient](https://github.com/Omie/rrdaclient) - Go Library to access statdns.com API, which is in turn RRDA API. DNS Queries over HTTP. - :arrow_down:0 - :star:3
* [shopify](https://github.com/rapito/go-shopify) - Go Library to make CRUD request to the Shopify API.
* [slack](https://github.com/nlopes/slack) - Slack API in Go. - :arrow_down:343 - :star:645
* [smite](https://github.com/sergiotapia/smitego) - Go package to wraps access to the Smite game API. - :arrow_down:0 - :star:6
* [spotify](https://github.com/rapito/go-spotify) - Go Library to access Spotify WEB API.
* [steam](https://github.com/sostronk/go-steam) - Go Library to interact with Steam game servers. - :arrow_down:0 - :star:7
* [stripe](https://github.com/stripe/stripe-go) - Go client for the Stripe API - :arrow_down:1407 - :star:448
* [telebot](https://github.com/tucnak/telebot) - Telegram bot framework written in Go. - :arrow_down:57 - :star:229
* [telegram-bot-api](https://github.com/Syfaro/telegram-bot-api) - Simple and clean Telegram bot client. - :arrow_down:31 - :star:304
* [textbelt](https://github.com/dietsche/textbelt) - Go client for the textbelt.com txt messaging API. - :arrow_down:0 - :star:5
* [TheMovieDb](https://github.com/jbrodriguez/go-tmdb) - A simple golang package to communicate with [themoviedb.org](https://themoviedb.org) - :arrow_down:0 - :star:5
* [translate](https://github.com/poorny/translate) - Go online translation package. - :arrow_down:0 - :star:13
* [tumblr](https://github.com/mattcunningham/gumblr) - Go wrapper for the Tumblr v2 API. - :arrow_down:0 - :star:1
* [webhooks](https://github.com/go-playground/webhooks) - Webhook receiver for GitHub and Bitbucket. - :arrow_down:0 - :star:29

## Utilities

*General utilities and tools to make your life easier.*

* [abutil](https://github.com/bahlo/abutil) - A collection of often-used Golang helpers. - :arrow_down:0 - :star:9
* [apm](https://github.com/topfreegames/apm) - A process manager for Golang applications with an HTTP API. - :arrow_down:0 - :star:54
* [boilr](https://github.com/tmrts/boilr) - A blazingly fast CLI tool for creating projects from boilerplate templates. - :arrow_down:0 - :star:257
* [command](https://github.com/txgruppi/command) - Command pattern for Go with thread safe serial and parallel dispatcher - :arrow_down:0 - :star:1
* [coop](https://github.com/rakyll/coop) - Cheat sheet for some of the common concurrent flows in Go. - :arrow_down:2 - :star:1158
* [Death](https://github.com/vrecan/death) - Managing go application shutdown with signals. - :arrow_down:4 - :star:42
* [Deepcopier](https://github.com/ulule/deepcopier) - Simple struct copying for Go. - :arrow_down:2 - :star:86
* [delve](https://github.com/derekparker/delve) - Go debugger.
* [dlog](https://github.com/kirillDanshin/dlog) - Compile-time controlled logger to make your release smaller without removing debug calls. - :arrow_down:1 - :star:3
* [fastlz](https://github.com/digitalcrab/fastlz) - Wrap over [FastLz](http://fastlz.org/) (free, open-source, portable real-time compression library) for GoLang. - :arrow_down:0 - :star:6
* [filetype](https://github.com/h2non/filetype) - Small package to infer the file type checking the magic numbers signature. - :arrow_down:0 - :star:70
* [fzf](https://github.com/junegunn/fzf) - A command-line fuzzy finder written in Go
* [generate](https://github.com/go-playground/generate) - runs go generate recursively on a specified path or environment variable and can filter by regex. - :arrow_down:0 - :star:1
* [gentleman](https://github.com/h2non/gentleman) - Full-featured plugin-driven HTTP client library. - :arrow_down:0 - :star:303
* [git-time-metric](https://github.com/git-time-metric/gtm) - Simple, seamless, lightweight time tracking for Git - :arrow_down:0 - :star:209
* [go-bind-plugin](https://github.com/wendigo/go-bind-plugin) - go:generate tool for wrapping symbols exported by golang plugins (1.8 only) - :arrow_down:0 - :star:84
* [go-cron](https://github.com/rk/go-cron) - A simple Cron library for go that can execute closures or functions at varying intervals, from once a second to once a year on a specific date and time. Primarily for web applications and long running daemons. - :arrow_down:2 - :star:123
* [go-debug](https://github.com/tj/go-debug) - Conditional debug logging for Golang libraries & applications. - :arrow_down:100 - :star:329
* [go-dry](https://github.com/ungerik/go-dry) - DRY (don't repeat yourself) package for Go. - :arrow_down:40 - :star:166
* [go-rate](https://github.com/beefsack/go-rate) -  A timed rate limiter for Go. - :arrow_down:12 - :star:195
* [go-sitemap-generator](https://github.com/ikeikeikeike/go-sitemap-generator) - XML Sitemap generator written in Go.
* [go-torch](https://github.com/uber/go-torch) - Stochastic flame graph profiler for Go programs. - :arrow_down:0 - :star:1452
* [go-trigger](https://github.com/sadlil/go-trigger) - Go-lang global event triggerer, Register Events with an id and trigger the event from anywhere from your project. - :arrow_down:0 - :star:51
* [go-underscore](https://github.com/tobyhede/go-underscore) - A useful collection of helpfully functional Go collection utilities. - :arrow_down:1 - :star:866
* [goback](https://github.com/carlescere/goback) - Go simple exponential backoff package. - :arrow_down:5 - :star:25
* [godaemon](https://github.com/VividCortex/godaemon) - Utility to write daemons. - :arrow_down:22 - :star:267
* [godotenv](https://github.com/joho/godotenv) - A Go port of Ruby's dotenv library (Loads environment variables from `.env`.) - :arrow_down:286 - :star:348
* [godropbox](https://github.com/dropbox/godropbox) - Common libraries for writing Go services/applications from Dropbox. - :arrow_down:0 - :star:3135
* [gohper](https://github.com/cosiner/gohper) - Various tools/modules help for development.
* [gojq](https://github.com/elgs/gojq) - JSON query in Golang. - :arrow_down:7 - :star:44
* [golarm](https://github.com/msempere/golarm) - Fire alarms with system events. - :arrow_down:1 - :star:19
* [golog](https://github.com/mlimaloureiro/golog) - Easy and lightweight CLI tool to time track your tasks. - :arrow_down:0 - :star:22
* [gopencils](https://github.com/bndr/gopencils) - Small and simple package to easily consume REST APIs. - :arrow_down:26 - :star:358
* [goplaceholder](https://github.com/michiwend/goplaceholder) - a small golang lib to generate placeholder images. - :arrow_down:6 - :star:11
* [goreq](https://github.com/franela/goreq) - Minimal and simple request library for Go language. - :arrow_down:101 - :star:504
* [goreq](https://github.com/smallnest/goreq) - An enhanced simplified HTTP client based on gorequest. - :arrow_down:0 - :star:25
* [gorequest](https://github.com/parnurzeal/gorequest) - Simplified HTTP client with rich features for Go. - :arrow_down:271 - :star:857
* [gotenv](https://github.com/subosito/gotenv) - Load environment variables from `.env` or any `io.Reader` in Go - :arrow_down:21 - :star:50
* [grequests](https://github.com/levigross/grequests) - An elegant and simple `net/http` wrapper that follows Python's requests library - :arrow_down:26 - :star:750
* [htcat](https://github.com/htcat/htcat) - Parallel and Pipelined HTTP GET Utility - :arrow_down:4 - :star:422
* [httpcontrol](https://github.com/facebookgo/httpcontrol) - Package httpcontrol allows for HTTP transport level control around timeouts and retries. - :arrow_down:35 - :star:429
* [hystrix-go](https://github.com/afex/hystrix-go) - Implements Hystrix patterns of programmer-defined fallbacks aka circuit breaker.
* [JobRunner](https://github.com/bamzi/jobrunner) - Smart and featureful cron job scheduler with job queuing and live monitoring built in. - :arrow_down:16 - :star:296
* [jsonapi-errors](https://github.com/AmuzaTkts/jsonapi-errors) - Go bindings based on the JSON API errors reference. - :arrow_down:0 - :star:0
* [jsonf](https://github.com/miolini/jsonf) - Console tool for highlighted formatting and struct query fetching JSON. - :arrow_down:0 - :star:29
* [jsongo](https://github.com/ricardolonga/jsongo) - Fluent API to make it easier to create Json objects. - :arrow_down:0 - :star:51
* [kazaam](https://github.com/Qntfy/kazaam) - API for arbitrary transformation of JSON documents.
* [lrserver](https://github.com/jaschaephraim/lrserver) - LiveReload server for Go - :arrow_down:10 - :star:70
* [mc](https://github.com/minio/mc) - Minio Client provides minimal tools to work with Amazon S3 compatible cloud storage and filesystems. - :arrow_down:0 - :star:341
* [mergo](https://github.com/imdario/mergo) - A helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements. - :arrow_down:461 - :star:163
* [minify](https://github.com/tdewolff/minify) - Fast minifiers for HTML, CSS, JS, XML, JSON and SVG file formats. - :arrow_down:86 - :star:665
* [moldova](https://github.com/StabbyCutyou/moldova) - A utility for generating random data based on an input template. - :arrow_down:0 - :star:119
* [mp](https://github.com/sanbornm/mp) - A simple cli email parser. It currently takes stdin and outputs JSON. - :arrow_down:0 - :star:14
* [multitick](https://github.com/VividCortex/multitick) - Multiplexor for aligned tickers. - :arrow_down:1 - :star:44
* [netbug](https://github.com/e-dard/netbug) - Easy remote profiling of your services. - :arrow_down:0 - :star:40
* [ngrok](https://github.com/inconshreveable/ngrok) - Introspected tunnels to localhost.
* [okrun](https://github.com/xta/okrun) - go run error steamroller. - :arrow_down:0 - :star:11
* [panicparse](https://github.com/maruel/panicparse) - Groups similar goroutines and colorizes stack dump. - :arrow_down:0 - :star:1290
* [peco](https://github.com/peco/peco) - Simplistic interactive filtering tool. - :arrow_down:3 - :star:3104
* [pester](https://github.com/sethgrid/pester) - Go HTTP client calls with retries, backoff, and concurrency. - :arrow_down:24 - :star:85
* [pm](https://github.com/VividCortex/pm) - Process (i.e. goroutine) manager with an HTTP API. - :arrow_down:3 - :star:40
* [profile](https://github.com/davecheney/profile) - Simple profiling support package for Go.
* [realize](https://github.com/tockins/realize) - Go build system with file watchers and live reload. Run, build and watch file changes with custom paths. - :arrow_down:0 - :star:667
* [request](https://github.com/mozillazg/request) - Go HTTP Requests for Humans™. - :arrow_down:7 - :star:148
* [rerate](https://github.com/abo/rerate) - Redis-based rate counter and rate limiter for Go. - :arrow_down:1 - :star:5
* [rerun](https://github.com/ivpusic/rerun) - Recompiling and rerunning go apps when source changes. - :arrow_down:0 - :star:111
* [resty](https://github.com/go-resty/resty) - Simple HTTP and REST client for Go inspired by Ruby rest-client. - :arrow_down:13 - :star:320
* [robustly](https://github.com/VividCortex/robustly) - Runs functions resiliently, catching and restarting panics. - :arrow_down:2 - :star:107
* [scheduler](https://github.com/carlescere/scheduler) - Cronjobs scheduling made easy. - :arrow_down:12 - :star:103
* [sling](https://github.com/dghubble/sling) - Go HTTP requests builder for API clients. - :arrow_down:64 - :star:370
* [spinner](https://github.com/briandowns/spinner) - Go package to easily provide a terminal spinner with options. - :arrow_down:32 - :star:258
* [sqlx](https://github.com/jmoiron/sqlx) - provides a set of extensions on top of the excellent built-in database/sql package. - :arrow_down:1101 - :star:2005
* [toolbox](https://github.com/viant/toolbox) - Slice, map, multimap, struct, function, data conversion utilities. Service router, macro evaluator, tokenizer. - :arrow_down:6 - :star:2
* [ugo](https://github.com/alxrm/ugo) - ugo is slice toolbox with concise syntax for Go. - :arrow_down:0 - :star:10
* [xferspdy](https://github.com/monmohan/xferspdy) - Xferspdy provides binary diff and patch library in golang - :arrow_down:0 - :star:12
* [xlsx](https://github.com/tealeg/xlsx) - Library to simplify reading the XML format used by recent version of Microsoft Excel in Go programs. - :arrow_down:171 - :star:1261


## Validation

*Libraries for validation.*

* [govalidator](https://github.com/asaskevich/govalidator) - Validators and sanitizers for strings, numerics, slices and structs. - :arrow_down:332 - :star:1270
* [ozzo-validation](https://github.com/go-ozzo/ozzo-validation) - Supports validation of various data types (structs, strings, maps, slices, etc.) with configurable and extensible validation rules specified in usual code constructs instead of struct tags. - :arrow_down:6 - :star:23
* [validator](https://github.com/go-playground/validator) - Go Struct and Field validation, including Cross Field, Cross Struct, Map, Slice and Array diving. - :arrow_down:1 - :star:685


## Version Control

*Libraries for version control.*

* [gh](https://github.com/rjeczalik/gh) - Scriptable server and net/http middleware for GitHub Webhooks. - :arrow_down:0 - :star:41
* [git2go](https://github.com/libgit2/git2go) - Go bindings for libgit2. - :arrow_down:129 - :star:875
* [go-vcs](https://github.com/sourcegraph/go-vcs) - manipulate and inspect VCS repositories in Go.
* [hgo](https://github.com/beyang/hgo) - Hgo is a collection of Go packages providing read-access to local Mercurial repositories. - :arrow_down:4 - :star:8


## Video

*Libraries for manipulating video.*

* [gmf](https://github.com/3d0c/gmf) - Go bindings for FFmpeg av\* libraries. - :arrow_down:18 - :star:230
* [goav](https://github.com/giorgisio/goav) - Comphrensive Go bindings for FFmpeg. - :arrow_down:0 - :star:205
* [gst](https://github.com/ziutek/gst) - Go bindings for GStreamer. - :arrow_down:19 - :star:117
* [v4l](https://github.com/korandiz/v4l) - A video capture library for Linux, written in Go. - :arrow_down:2 - :star:0


## Web Frameworks

*Full stack web frameworks.*

* [alien](https://github.com/gernest/alien) - A lightweight and  fast http router from outer space - :arrow_down:0 - :star:62
* [Beego](https://github.com/astaxie/beego) - beego is an open-source, high-performance web framework for the Go programming language. - :arrow_down:4739 - :star:8099
* [Bone](https://github.com/go-zoo/bone) - Lightning Fast HTTP Multiplexer. - :arrow_down:101 - :star:924
* [Bxog](https://github.com/claygod/Bxog) - Simple and fast HTTP router for Go. It works with routes of varying difficulty, length and nesting. And he knows how to create a URL from the received parameters. - :arrow_down:4 - :star:53
* [chi](https://github.com/pressly/chi) - Small, fast and expressive HTTP router built on net/context. - :arrow_down:71 - :star:424
* [Echo](https://github.com/labstack/echo) - A fast and unfancy micro web framework for Go. - :arrow_down:1152 - :star:5237
* [fasthttprouter](https://github.com/buaazp/fasthttprouter) - A high performance router forked from `httprouter`. The first router fit for `fasthttp`. - :arrow_down:21 - :star:141
* [Fireball](https://github.com/zpatrick/fireball) - A more "natural" feeling web framework. - :arrow_down:0 - :star:1
* [Florest](https://github.com/jabong/florest-core) - High-performance workflow based REST API framework
* [Gem](https://github.com/go-gem/gem) - A simple and fast web framework, friendly to REST API.
* [Gin](https://github.com/gin-gonic/gin) - Gin is a web framework written in Go! It features a martini-like API with much better performance, up to 40 times faster. If you need performance and good productivity. - :arrow_down:3959 - :star:7720
* [Gizmo](https://github.com/NYTimes/gizmo) - Microservice toolkit used by the New York Times. - :arrow_down:0 - :star:1506
* [Glue](https://github.com/desertbit/glue) - Robust Go and Javascript Socket Library (Alternative to Socket.io). - :arrow_down:13 - :star:186
* [go-json-rest](https://github.com/ant0ine/go-json-rest) - A quick and easy way to setup a RESTful JSON API.
* [go-kit](https://github.com/go-kit/kit) - A Microservice toolkit with support for service discovery, load balancing, pluggable transports, request tracking, etc.
* [go-relax](https://github.com/codehack/go-relax) - A framework of pluggable components to build RESTful API's. - :arrow_down:10 - :star:126
* [go-rest](https://github.com/ungerik/go-rest) - A small and evil REST framework for Go. - :arrow_down:11 - :star:95
* [go-socket.io](https://github.com/googollee/go-socket.io) - socket.io library for golang, a realtime application framework. - :arrow_down:178 - :star:1397
* [goa](https://github.com/raphael/goa) - Framework for developing microservices based on the design of Ruby's Praxis. - :arrow_down:34 - :star:1346
* [Goat](https://github.com/bahlo/goat) - A minimalistic REST API server in Go. - :arrow_down:5 - :star:97
* [gocraft/web](https://github.com/gocraft/web) - A mux and middleware package in Go. - :arrow_down:209 - :star:1131
* [Goji](https://github.com/goji/goji) - Goji is a minimalistic and flexible HTTP request multiplexer with support for `net/context`. - :arrow_down:0 - :star:303
* [Golf](https://github.com/dinever/golf) - Golf is a fast, simple and lightweight micro-web framework for Go. It comes with powerful features and has no dependencies other than the Go Standard Library. - :arrow_down:25 - :star:179
* [golongpoll](https://github.com/jcuga/golongpoll) - HTTP longpoll server library that makes web pub-sub simple. - :arrow_down:4 - :star:296
* [Gondola](https://github.com/rainycape/gondola) - The web framework for writing faster sites, faster - :arrow_down:0 - :star:298
* [gongular](https://github.com/mustafaakin/gongular) - A fast Go web framework with input mapping/validation and (DI) Dependency Injection - :arrow_down:2 - :star:220
* [goose](https://github.com/ian-kent/goose) - Server Sent Events in Go - :arrow_down:6 - :star:23
* [Gorilla](https://github.com/gorilla/) - Gorilla is a web toolkit for the Go programming language.
* [httprouter](https://github.com/julienschmidt/httprouter) - A high performance router. Use this and the standard http handlers to form a very high performance web framework. - :arrow_down:2453 - :star:3629
* [httptreemux](https://github.com/dimfeld/httptreemux) - High-speed, flexible tree-based HTTP router for Go. Inspiration from httprouter. - :arrow_down:142 - :star:171
* [lars](https://github.com/go-playground/lars) - Is a lightweight, fast and extensible zero allocation HTTP router for Go used to create customizable frameworks. - :arrow_down:37 - :star:306
* [Macaron](https://github.com/go-macaron/macaron) - Macaron is a high productive and modular design web framework in Go. - :arrow_down:10 - :star:1219
* [mango](https://github.com/paulbellamy/mango) - Mango is a modular web-application framework for Go, inspired by Rack, and PEP333. - :arrow_down:77 - :star:304
* [medeina](https://github.com/imdario/medeina) - Medeina is a HTTP routing tree based on HttpRouter, inspired by Roda and Cuba. - :arrow_down:1 - :star:16
* [mux](https://github.com/gorilla/mux) - A powerful URL router and dispatcher for golang. - :arrow_down:8786 - :star:2741
* [neo](https://github.com/ivpusic/neo) - Neo is minimal and fast Go Web Framework with extremely simple API. - :arrow_down:16 - :star:276
* [ozzo-routing](https://github.com/go-ozzo/ozzo-routing) - A high-performance HTTP router and Web framework supporting routes with regular expressions. Comes with full support for quickly building a RESTful API application. - :arrow_down:45 - :star:108
* [pat](https://github.com/bmizerany/pat) - Sinatra style pattern muxer for Go’s net/http library, by the author of Sinatra. - :arrow_down:560 - :star:978
* [Resoursea](https://github.com/resoursea/api) - A REST framework for quickly writing resource based services. - :arrow_down:2 - :star:25
* [REST Layer](http://rest-layer.io) - A framework to build REST/GraphQL API on top of databases with mostly configuration over code.
* [Revel](https://github.com/revel/revel) - A high-productivity web framework for the Go language. - :arrow_down:1249 - :star:7262
* [rex](https://github.com/goanywhere/rex) - Rex is a library for modular development built upon gorilla/mux, fully compatible with `net/http`. - :arrow_down:3 - :star:11
* [sawsij](http://sawsij.com/) - lightweight, open-source web framework for building high-performance, data-driven web applications.
* [session](https://github.com/icza/session) - Go session management for web servers (including support for Google App Engine - GAE). - :arrow_down:1 - :star:6
* [Siesta](https://github.com/VividCortex/siesta) - Composable framework to write middleware and handlers - :arrow_down:8 - :star:337
* [tango](https://github.com/lunny/tango) - Micro & pluggable web framework for Go. - :arrow_down:132 - :star:454
* [tigertonic](https://github.com/rcrowley/go-tigertonic) - A Go framework for building JSON web services inspired by Dropwizard - :arrow_down:133 - :star:943
* [traffic](https://github.com/pilu/traffic) - Sinatra inspired regexp/pattern mux and web framework for Go. - :arrow_down:76 - :star:486
* [utron](https://github.com/gernest/utron) - A lightweight MVC framework for Go(Golang). - :arrow_down:9 - :star:1615
* [VarHandler](https://github.com/azr/generators/tree/master/varhandler) - Generate boilerplate http input and ouput handling.
* [vestigo](https://github.com/husobee/vestigo) -  A performant, stand-alone, HTTP compliant URL Router for go web applications. - :arrow_down:15 - :star:68
* [Volatile](https://github.com/volatile/core) - Minimalist middleware stack promoting flexibility, good practices and clean code. - :arrow_down:14 - :star:80
* [xmux](https://github.com/rs/xmux) - A high performance muxer based on `httprouter` with `net/context` support. - :arrow_down:7 - :star:62
* [YARF](https://github.com/yarf-framework/yarf) - Fast micro-framework designed to build REST APIs and web services in a fast and simple way. - :arrow_down:8 - :star:25
* [Zerver](https://github.com/cosiner/zerver) - Zerver is an expressive, modular, feature completed RESTful framework. - :arrow_down:10 - :star:136
* [zeus](https://github.com/daryl/zeus) - A very simple and fast HTTP router for Go. - :arrow_down:16 - :star:98


### Middlewares

#### Actual middlewares

* [CORS](https://github.com/rs/cors) - Easily add CORS capabilities to your API. - :arrow_down:387 - :star:361
* [formjson](https://github.com/rs/formjson) - Transparently handle JSON input as a standard form POST. - :arrow_down:0 - :star:20
* [Limiter](https://github.com/ulule/limiter) - Dead simple rate limit middleware for Go. - :arrow_down:2 - :star:226
* [Tollbooth](https://github.com/didip/tollbooth) - Rate limit HTTP request handler. - :arrow_down:13 - :star:410
* [XFF](https://github.com/sebest/xff) - Handle `X-Forwarded-For` header and friends. - :arrow_down:11 - :star:51

#### Libraries for creating HTTP middlewares

* [alice](https://github.com/justinas/alice) - Painless middleware chaining for Go. - :arrow_down:265 - :star:988
* [catena](https://github.com/codemodus/catena) - http.Handler wrapper catenation (same API as "chain"). - :arrow_down:0 - :star:6
* [chain](https://github.com/codemodus/chain) - Handler wrapper chaining with scoped data (net/context-based "middleware"). - :arrow_down:2 - :star:61
* [go-wrap](https://github.com/go-on/wrap) - Small middlewares package for net/http. - :arrow_down:1 - :star:52
* [gores](https://github.com/alioygur/gores) - Go package that handles HTML, JSON, XML and etc. responses. Useful for RESTful APIs. - :arrow_down:1 - :star:43
* [interpose](https://github.com/carbocation/interpose) - Minimalist net/http middleware for golang. - :arrow_down:69 - :star:261
* [muxchain](https://github.com/stephens2424/muxchain) - Lightweight middleware for net/http. - :arrow_down:5 - :star:197
* [negroni](https://github.com/urfave/negroni) - Idiomatic HTTP middleware for Golang. - :arrow_down:79 - :star:3933
* [render](https://github.com/unrolled/render) - Go package for easily rendering JSON, XML, and HTML template responses. - :arrow_down:397 - :star:725
* [rye](https://github.com/InVisionApp/rye) - Tiny Go middleware library (with canned Middlewares) that supports JWT, CORS, Statsd, and Go 1.7 context
* [stats](https://github.com/thoas/stats) - A Go middleware that stores various information about your web application. - :arrow_down:120 - :star:363

# Tools

Go software and plugins.


## Code Analysis

* [apicompat](https://github.com/bradleyfalzon/apicompat) - Checks recent changes to a Go project for backwards incompatible changes. - :arrow_down:0 - :star:42
* [dupl](https://github.com/mibk/dupl) - A tool for code clone detection. - :arrow_down:0 - :star:61
* [errcheck](https://github.com/kisielk/errcheck) - Errcheck is a program for checking for unchecked errors in Go programs. - :arrow_down:0 - :star:674
* [gcvis](https://github.com/davecheney/gcvis) - Visualise Go program GC trace data in real time. - :arrow_down:0 - :star:586
* [Go Metalinter](https://github.com/alecthomas/gometalinter) - Metalinter is a tool to automatically apply all static analysis tool and report their output in normalized form. - :arrow_down:0 - :star:1174
* [go-checkstyle](https://github.com/qiniu/checkstyle) checkstyle is a style check tool like java checkstyle. This tool inspired by java checkstyle, golint. The style refered to some points in Go Code Review Comments. - :arrow_down:5 - :star:30
* [go-outdated](https://github.com/firstrow/go-outdated) - Console application that displays outdated packages. - :arrow_down:0 - :star:28
* [goast-viewer](https://github.com/yuroyoro/goast-viewer) - Web based Golang AST visualizer. - :arrow_down:0 - :star:143
* [GoCover.io](http://gocover.io/) - GoCover.io offers the code coverage of any golang package as a service.
* [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports) - Tool to fix (add, remove) your Go imports automatically.
* [GoLint](https://github.com/golang/lint) - Golint is a linter for Go source code. - :arrow_down:105 - :star:1467
* [Golint online](http://go-lint.appspot.com/) - Lints online Go source files on GitHub, Bitbucket and Google Project Hosting using the golint package.
* [goreturns](https://sourcegraph.com/github.com/sqs/goreturns) - Adds zero-value return statements to match the func return types.
* [gostatus](https://github.com/shurcooL/gostatus) - A command line tool, shows the status of repositories that contain Go packages. - :arrow_down:0 - :star:173
* [interfacer](https://github.com/mvdan/interfacer) - A linter that suggests interface types. - :arrow_down:0 - :star:485
* [lint](https://github.com/surullabs/lint) - Run linters as part of go test - :arrow_down:2 - :star:45
* [validate](https://github.com/mccoyst/validate) - Automatically validates struct fields with tags. - :arrow_down:3 - :star:57


## Editor Plugins

* [go-lang-idea-plugin](https://github.com/go-lang-plugin-org/go-lang-idea-plugin) Go plugin for IntelliJ IDEA.
* [go-plus](https://github.com/joefitzgerald/go-plus) - Go (Golang) Package For Atom That Adds Autocomplete, Formatting, Syntax Checking, Linting and Vetting
* [Goclipse](https://github.com/GoClipse/goclipse) - An Eclipse plugin for Go.
* [gocode](https://github.com/nsf/gocode) - An autocompletion daemon for the Go programming language. - :arrow_down:0 - :star:3311
* [GoSublime](https://github.com/DisposaBoy/GoSublime) - A Golang plugin collection for the text editor SublimeText 2 providing code completion and other IDE-like features.
* [velour](https://github.com/velour/velour) - An IRC client for the acme editor. - :arrow_down:0 - :star:13
* [vim-compiler-go](https://github.com/rjohnsondev/vim-compiler-go) - A Vim plugin to highlight syntax errors on save.
* [vim-go](https://github.com/fatih/vim-go) - Go development plugin for Vim.
* [Watch](https://github.com/eaburns/Watch) - Runs a command in an acme win on file changes. - :arrow_down:0 - :star:114

## Go Tools

* [colorgo](https://github.com/songgao/colorgo) - A wrapper around `go` command for colorized `go build` output. - :arrow_down:0 - :star:69
* [gb](https://getgb.io/) - An easy to use project based build tool for the Go programming language.
* [go-pkg-complete](https://github.com/skelterjohn/go-pkg-complete) - Bash completion for go and wgo.
* [go-swagger](https://github.com/go-swagger/go-swagger) - Swagger 2.0 implementation for go. Swagger is a simple yet powerful representation of your RESTful API. - :arrow_down:5 - :star:716
* [rts](https://github.com/galeone/rts) - RTS: response to struct. Generates Go structs from server responses. - :arrow_down:0 - :star:111

## Software Packages

Software written in Go.


### DevOps Tools

* [aptly](https://github.com/smira/aptly) - aptly is a Debian repository management tool. - :arrow_down:0 - :star:1124
* [awsenv](https://github.com/soniah/awsenv) - a small binary that loads Amazon (AWS) environment variables for a profile. - :arrow_down:0 - :star:8
* [Banshee](https://github.com/eleme/banshee) - Anomalies detection system for periodic metrics. - :arrow_down:0 - :star:328
* [bosun](https://github.com/bosun-monitor/bosun) - Time Series Alerting Framework.
* [dogo](https://github.com/liudng/dogo) - Monitoring changes in the source file and automatically compile and run (restart). - :arrow_down:0 - :star:117
* [Dropship](https://github.com/chrismckenzie/dropship) - A tool for deploying code via cdn.
* [EasySSH](https://github.com/hypersleep/easyssh) - Golang package for easy remote execution through SSH and SCP downloading. - :arrow_down:13 - :star:128
* [Gitea](https://github.com/go-gitea/gitea) - A fork of Gogs, entirely community driven. - :arrow_down:0 - :star:249
* [Go Metrics](https://github.com/rcrowley/go-metrics) - Go port of Coda Hale's Metrics library: https://github.com/codahale/metrics. - :arrow_down:1159 - :star:1327
* [go-selfupdate](https://github.com/sanbornm/go-selfupdate) - Enable your Go applications to self update. - :arrow_down:0 - :star:396
* [gobrew](https://github.com/cryptojuice/gobrew) - gobrew lets you easily switch between multiple versions of go.
* [godbg](https://github.com/sirnewton01/godbg) - Web-based gdb front-end application. - :arrow_down:1 - :star:191
* [Gogs](https://gogs.io/) - A Self Hosted Git Service in the Go Programming Language.
* [gonative](https://github.com/inconshreveable/gonative) - Tool which creates a build of Go that can cross compile to all platforms while still using the Cgo-enabled versions of the stdlib packages. - :arrow_down:0 - :star:241
* [govvv](https://github.com/ahmetalpbalkan/govvv) - A “go build” wrapper to easily add version information into Go binaries - :arrow_down:0 - :star:81
* [gox](https://github.com/mitchellh/gox) - A dead simple, no frills Go cross compile tool. - :arrow_down:0 - :star:1794
* [goxc](https://github.com/laher/goxc) - build tool for Go, with a focus on cross-compiling and packaging. - :arrow_down:0 - :star:1332
* [grapes](https://github.com/yaronsumel/grapes) -  lightweight tool designed to distribute commands over ssh with ease. - :arrow_down:0 - :star:24
* [GVM](https://github.com/moovweb/gvm) - GVM provides an interface to manage Go versions.
* [Hey](https://github.com/rakyll/hey) - Hey is a tiny program that sends some load to a web application. - :arrow_down:0 - :star:261
* [kala](https://github.com/ajvb/kala) - Simplistic, modern, and performant job scheduler. - :arrow_down:0 - :star:869
* [kubernetes](https://github.com/kubernetes/kubernetes) - Container Cluster Manager from Google.
* [Mora](https://github.com/emicklei/mora) - REST server for accessing MongoDB documents and meta data. - :arrow_down:0 - :star:164
* [ostent](https://github.com/ostrost/ostent) - collects and displays system metrics and optionally relays to Graphite and/or InfluxDB. - :arrow_down:0 - :star:69
* [Packer](https://github.com/mitchellh/packer) - Packer is a tool for creating identical machine images for multiple platforms from a single source configuration. - :arrow_down:0 - :star:5674
* [Rodent](https://github.com/alouche/rodent) - Rodent helps you manage Go versions, projects and track dependencies.
* [s3gof3r](https://github.com/rlmcpherson/s3gof3r) - A small utility/library optimized for high speed transfer of large objects into and out of Amazon S3. - :arrow_down:50 - :star:731
* [Scaleway-cli](https://github.com/scaleway/scaleway-cli) - Manage BareMetal Servers from Command Line (as easily as with Docker). - :arrow_down:0 - :star:162
* [sg](https://github.com/ChristopherRabotin/sg) - Benchmarks a set of HTTP endpoints (like ab), with possibility to use the reponse code and data between each call for specific server stress based on its previous response. - :arrow_down:0 - :star:0
* [Vegeta] (https://github.com/tsenart/vegeta) - HTTP load testing tool and library. It's over 9000!
* [webhook](https://github.com/adnanh/webhook) - Tool which allows user to create HTTP endpoints (hooks) that execute commands on the server. - :arrow_down:0 - :star:493
* [Wide](https://wide.b3log.org/login) - A Web-based IDE for Teams using Golang.
* [winrm-cli](https://github.com/masterzen/winrm-cli) - A cli tool to remotely execute commands on Windows machines

### Other Software
* [borg](https://github.com/crufter/borg) - A terminal based search engine for bash snippets - :arrow_down:0 - :star:906
* [boxed](https://github.com/tejo/boxed) - Dropbox based blog engine - :arrow_down:0 - :star:55
* [Cherry](https://github.com/rafael-santiago/cherry) - A tiny webchat server in Go.
* [Circuit](https://github.com/gocircuit/circuit) - Circuit is a programmable platform-as-a-service (PaaS) and/or Infrastructure-as-a-Service (IaaS), for management, discovery, synchronization and orchestration of services and hosts comprising cloud applications.
* [Comcast](https://github.com/tylertreat/Comcast) - Simulate bad network connections.
* [confd](https://github.com/kelseyhightower/confd) - Manage local application configuration files using templates and data from etcd or consul. - :arrow_down:0 - :star:3155
* [Docker](http://www.docker.com/) - An open platform for distributed applications for developers and sysadmins.
* [Documize](https://github.com/documize/community) - Modern wiki software that integrates data from SaaS tools.
* [fleet](https://github.com/coreos/fleet) - A Distributed init System. - :arrow_down:0 - :star:2306
* [Go Package Store](https://github.com/shurcooL/Go-Package-Store#go-package-store-) - An app that displays updates for the Go packages in your GOPATH. - :arrow_down:8 - :star:681
* [gocc](https://github.com/goccmack/gocc) - Gocc is a compiler kit for Go written in Go. - :arrow_down:0 - :star:57
* [GoDocTooltip](https://github.com/diankong/GoDocTooltip) - A chrome extension for Go Doc sites, which shows function description as tooltip at funciton list.
* [Gor](https://github.com/buger/gor) - Http traffic replication tool, for replaying traffic from production to stage/dev environments in real-time. - :arrow_down:4 - :star:6206
* [hsync](http://ambrevar.bitbucket.org/hsync/) - A filesystem hierarchy synchronizer.
* [hugo](http://gohugo.io/) - A Fast and Modern Static Website Engine.
* [ipe](https://github.com/dimiro1/ipe) - An open source Pusher server implementation compatible with Pusher client libraries written in GO. - :arrow_down:0 - :star:162
* [Juju](https://jujucharms.com/) - Cloud-agnostic service deployment and orchestration - supports EC2, Azure, Openstack, MAAS and more.
* [limetext](http://limetext.org/) Lime Text is a powerful and elegant text editor primarily developed in Go that aims to be a Free and open-source software successor to Sublime Text.
* [LiteIDE](https://github.com/visualfc/liteide) LiteIDE is a simple, open source, cross-platform Go IDE.
* [mockingjay](https://github.com/quii/mockingjay-server) Fake HTTP servers and consumer driven contracts from one configuration file. You can also make the server randomly misbehave to help do more realistic performance tests. - :arrow_down:0 - :star:260
* [myLG](https://github.com/mehrdadrad/mylg) - Command Line Network Diagnostic tool written in Go. - :arrow_down:0 - :star:973
* [naclpipe](https://github.com/unix4fun/naclpipe) - A simple NaCL EC25519 based crypto pipe tool written in Go. - :arrow_down:0 - :star:5
* [nes](https://github.com/fogleman/nes) - A Nintendo Entertainment System (NES) emulator written in Go. - :arrow_down:0 - :star:2357
* [orange-cat](https://github.com/noraesae/orange-cat) - A Markdown previewer written in Go. - :arrow_down:1 - :star:141
* [peg](https://github.com/pointlander/peg) - Peg, Parsing Expression Grammar, is an implementation of a Packrat parser generator. - :arrow_down:0 - :star:311
* [Postman](https://github.com/zachlatta/postman) - Command-line utility for batch-sending email. - :arrow_down:0 - :star:648
* [restic](https://github.com/restic/restic) - De-duplicating backup program. - :arrow_down:11 - :star:677
* [rkt](https://github.com/coreos/rkt) - An App Container runtime that integrates with init systems, is compatible with other container formats like Docker, and supports alternative execution engines like KVM.
* [Seaweed File System](https://github.com/chrislusf/seaweedfs) - Fast, Simple and Scalable Distributed File System with O(1) disk seek.
* [shell2http](https://github.com/msoap/shell2http) - Executing shell commands via http server (for prototyping or remote control). - :arrow_down:0 - :star:53
* [snap](https://github.com/intelsdi-x/snap) - A powerful telemetry framework. - :arrow_down:0 - :star:978
* [Stack Up](https://github.com/pressly/sup) - Stack Up, a super simple deployment tool - just Unix - think of it like 'make' for a network of servers. - :arrow_down:0 - :star:1256
* [syncthing](https://syncthing.net/) - An open, decentralized file synchronization tool and protocol.
* [Tenyks](https://github.com/kyleterry/tenyks) - Service oriented IRC bot using Redis and JSON for messaging. - :arrow_down:0 - :star:160
* [toto](https://github.com/blogcin/ToTo) - A simple proxy server written in Go language, can be used together with browser. - :arrow_down:0 - :star:12
* [toxiproxy](https://github.com/shopify/toxiproxy) - Proxy to simulate network and system conditions for automated tests.
* [tsuru](https://tsuru.io/) - An extensible and open source Platform as a Service software.
* [websysd](https://github.com/ian-kent/websysd) - Web based process manager (like Marathon or Upstart). - :arrow_down:0 - :star:24
* [wellington](https://github.com/wellington/wellington) - Sass project management tool, extends the language with sprite functions (like Compass). - :arrow_down:5 - :star:200







# Resources

Where to discover new Go libraries.


## Benchmarks

* [autobench](https://github.com/davecheney/autobench) - Framework to compare the performance between different Go versions.
* [go-benchmarks](https://github.com/tylertreat/go-benchmarks) - A few miscellaneous Go microbenchmarks. Compare some language features to alternative approaches. - :arrow_down:0 - :star:36
* [go-http-routing-benchmark](https://github.com/julienschmidt/go-http-routing-benchmark) - Go HTTP request router benchmark and comparison. - :arrow_down:0 - :star:759
* [go-type-assertion-benchmark](https://github.com/hgfischer/go-type-assertion-benchmark) - Naive performance test of two ways to do type assertion in Go. - :arrow_down:0 - :star:3
* [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) - Go web framework benchmark. - :arrow_down:0 - :star:177
* [go_serialization_benchmarks](https://github.com/alecthomas/go_serialization_benchmarks) - Benchmarks of Go serialization methods. - :arrow_down:0 - :star:375
* [gocostmodel](https://github.com/PuerkitoBio/gocostmodel) - Benchmarks of common basic operations for the Go language. - :arrow_down:0 - :star:47
* [golang-micro-benchmarks](https://github.com/amscanne/golang-micro-benchmarks) - Tiny collection of Go micro benchmarks. The intent is to compare some language features to others. - :arrow_down:0 - :star:5
* [golang-sql-benchmark](https://github.com/tyler-smith/golang-sql-benchmark) - A collection of benchmarks for popular Go database/SQL utilities.
* [gospeed](https://github.com/feyeleanor/GoSpeed) - Go micro-benchmarks for calculating the speed of language constructs.
* [kvbench](https://github.com/jimrobinson/kvbench) - Key/Value database benchmark. - :arrow_down:0 - :star:11
* [skynet](https://github.com/atemerev/skynet) - Skynet 1M threads microbenchmark.
* [speedtest-resize](https://github.com/fawick/speedtest-resize) - Compare various Image resize algorithms for the Go language. - :arrow_down:0 - :star:81


## Conferences

* [dotGo](http://www.dotgo.eu) - Paris, France
* [GoCon](http://gocon.connpass.com/) - Tokyo, Japan
* [GolangUK](http://golanguk.com/) - London, UK
* [GopherChina](http://gopherchina.org) - Shanghai, China
* [GopherCon](http://www.gophercon.com/) - Denver, USA
* [GopherCon Brazil](https://gopherconbr.org) - Florianópolis, BR
* [GopherCon Dubai](http://www.gophercon.ae/) - Dubai, UAE
* [GopherCon India](http://www.gophercon.in/) - Pune, India
* [GothamGo](http://gothamgo.com/) - New York City, USA

## E-Books

* [A Go Developer's Notebook](https://leanpub.com/GoNotebook/read)
* [An Introduction to Programming in Go](http://www.golang-book.com/)
* [Build Web Application with Golang](https://www.gitbook.com/book/astaxie/build-web-application-with-golang/details)
* [Building Web Apps With Go](https://www.gitbook.com/book/codegangsta/building-web-apps-with-go/details)
* [Go Bootcamp](http://golangbootcamp.com)
* [GoBooks](https://github.com/dariubs/GoBooks) - A curated list of Go books
* [Learning Go](https://www.miek.nl/downloads/Go/Learning-Go-latest.pdf)
* [Network Programming With Go](https://jan.newmarch.name/go/)
* [The Go Programming Language](http://www.gopl.io/)
* [Web Application with Go the Anti-Textbook](https://github.com/thewhitetulip/web-dev-golang-anti-textbook/)

## Twitter

* [@golang](https://twitter.com/golang)
* [@golang_news](https://twitter.com/golang_news)
* [@golangweekly](https://twitter.com/golangweekly)


## Websites

* [Awesome Go @LibHunt](https://go.libhunt.com) - Your go-to Go Toolbox.
* [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job) - A curated list of awesome remote jobs. A lot of them is looking for Go hackers.
* [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) - List of other amazingly awesome lists.
* [Flipboard - Go Magazine](https://flipboard.com/section/the-golang-magazine-bVP7nS) - A collection of Go articles and tutorials.
* [Go Blog](http://blog.golang.org) - The official Go blog.
* [Go Challenge](http://golang-challenge.org/) - Learn Go by solving problems and getting feedback from Go experts.
* [Go Forum](https://forum.golangbridge.org) - Forum to discuss Go.
* [Go In 5 Minutes](https://www.goin5minutes.com/) - 5 minute screencasts focused on getting one thing done.
* [Go Projects](https://github.com/golang/go/wiki/Projects) - List of projects on the Go community wiki.
* [gocryforhelp](https://github.com/ninedraft/gocryforhelp) - A collection of Go projects that needs help. Good place to start your open-source way in Go.
* [godoc.org](https://godoc.org/) - Documentation for open source Go packages.
* [golang-graphics](https://github.com/mholt/golang-graphics) - A collection of Go images, graphics, and art.
* [golang-nuts](https://groups.google.com/forum/#!forum/golang-nuts) - Go mailing list.
* [Google Plus Community](https://plus.google.com/communities/114112804251407510571) - The Google+ community for #golang enthusiasts.
* [gowalker.org](https://gowalker.org) - Go Project API documentation.
* [r/Golang](https://www.reddit.com/r/golang) - News about Go.
* [Trending Go repositories on GitHub today](https://github.com/trending?l=go) - Good place to find new Go libraries.


### Tutorials

* [A Tour of Go](http://tour.golang.org/) - Interactive tour of Go.
* [Building Go Web Applications and Microservices Using Gin](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin) - Get familiar with Gin and find out how it can help you reduce boilerplate code and build a request handling pipeline.
* [Go By Example](https://gobyexample.com/) - A hands-on introduction to Go using annotated example programs.
* [Go database/sql tutorial](http://go-database-sql.org/) - Introduction to database/sql.
* [How to Use Godog for Behavior-driven Development in Go](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go) - Get started with Godog — a Behavior-driven development framework for building and testing Go applications.
* [Working with Go](https://github.com/mkaz/working-with-go) - An intro to go for experienced programmers. - :arrow_down:0 - :star:551



## Windows

* [d3d9](https://github.com/gonutz/d3d9) - Go bindings for Direct3D9 - :arrow_down:1 - :star:28
* [go-ole](https://github.com/go-ole/go-ole) - Win32 OLE implementation for golang. - :arrow_down:44 - :star:230
