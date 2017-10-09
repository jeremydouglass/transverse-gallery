---
layout: post
title:  "Authorship in Gamebooks"
author: Sarah Oxford
categories: 
excerpt: ""
topics:
  packard-cyoa:
    images:
    -  image_path: 04-02 CYOA -- Who Are You.txt.gv.png
    -  image_path: 04-04 CYOA -- War with the Mutant Spider Ants.txt.gv.png
    -  image_path: 04-06 CYOA -- Cyberspace Warrior.txt.gv.png
    -  image_path: 04-08 CYOA -- You Are an Alien.txt.gv.png
    -  image_path: 04-10 CYOA -- Sky Jam.txt.gv.png
    -  image_path: 04-13 CYOA -- Typhoon.txt.gv.png
    -  image_path: 04-14 CYOA -- Shadow of the Swastika.txt.gv.png
    -  image_path: 04-15 CYOA -- Fright Night.txt.gv.png
    -  image_path: 04-19 CYOA -- Hostage.txt.gv.png
    -  image_path: 04-21 CYOA -- Greed, Guns, and Gold.txt.gv.png
    -  image_path: 04-23 CYOA -- Mountain Biker.txt.gv.png
    -  image_path: 04-25 CYOA -- The Power Dome.txt.gv.png
    -  image_path: 04-33 CYOA -- Fire on Ice.txt.gv.png
    -  image_path: 04-34 CYOA -- Fugitive.txt.gv.png
    -  image_path: 04-70 The Computer Takeover.txt.gv.png
  packard-other:
    images:
    -  image_path: 11-11v3 EFT 01 Tenopia Island (no maps, simplified).txt.gv.png
    -  image_path: 11-15 EFKF 01 Castle of Frome, The.txt.gv.png
  montgomery-cyoa:
    images:
    -  image_path: 03-10 CYOA -- Blood on the Handle.txt.gv.png
    -  image_path: 03-12 CYOA -- Stock Car Champion.txt.gv.png
    -  image_path: 03-25 CYOA -- Chinese Dragons.txt.gv.png
    -  image_path: 03-27 CYOA -- Smoke Jumper.txt.gv.png
    -  image_path: 03-31 CYOA -- Island of Time.txt.gv.png
    -  image_path: 03-37 CYOA -- Behind the Wheel.txt.gv.png
    -  image_path: 03-39 CYOA -- Silver Wings.txt.gv.png
    -  image_path: 03-55 CYOA -- Motocross Mania.txt.gv.png
    -  image_path: 03-59 CYOA -- Project UFO.txt.gv.png
    -  image_path: 04-05 CYOA -- Last Run.txt.gv.png
    -  image_path: 04-11 CYOA -- Tattoo of Death.txt.gv.png
    -  image_path: 04-12 CYOA -- Possessed.txt.gv.png
    -  image_path: 04-22 CYOA -- Death in the Dorm.txt.gv.png
    -  image_path: 04-29 CYOA -- Killer Virus.txt.gv.png
  montgomery-cyoa-dragonlarks:
    images:
    -  image_path: 42-36 CYOA - Dragonlarks 01 The Haunted House.txt.gv.png
    -  image_path: 42-37 CYOA - Dragonlarks 02 Your Very Own Robot.txt.gv.png
---

Within the Demian Katz Gamebook Collection, I began my research by encoding a large portion of the Choose Your Own Adventure (1979-1998) series. This series is comprised of gamebooks written by a handful of authors that incorporate various storylines. Although each book in the series is unrelated, they all carry the same basic series structure of page amounts, illustrations, branching narratives, and multiple endings. Under the blanket genre of adventure, some of these books break off into more specific sub-genres including mystery, historical fiction, western, science fiction, and fantasy.

### Two Authors

Edward Packard and R.A. Montgomery are two of the most prolific authors in not only the Choose Your Own Adventure series, but also in spin-off series as well as gamebooks in general. Just within the Demian Katz Gamebook Collection alone, there are 85 of Edward Packard’s works and 82 of R.A. Montgomery’s works. As I continued encoding my portion of the collection, I became more and more interested in comparative authorship. I questioned if an author’s writing style and narrative elements would manifest in a book’s encoded data or story graph.

In order to compare these two authors, I narrowed down the samples to a selection of 15 books per author. Edward Packard’s chosen samples include 13 Choose Your Own Adventure series books, one Escape from Tenopia series book, and one Escape from the Kingdom of Frome series book. R.A. Montgomery’s chosen samples include 13 Choose Your Own Adventure series books and two Choose Your Own Adventure: Dragonlarks series books. As I started studying each of the sample book’s graphs, I realized that the series itself was widely diverse in graph shapes. It really varied from book to book whether the graph would be more linear, arboreal, or web-like. Linear graphs have less nodes that break off into choices, which appears in the story graph’s length rather than its height. Arboreal graphs’ nodes are often choices, which gives the graph more branches. Web-like graphs do not flow in order, meaning that a later node can lead to an earlier node. This makes web-like graphs increasingly difficult to follow.

### Data

| R.A. MONGOMERY	| Nodes	| Average Degree	| General Shape |
|-----------------------|-------|-------|-------|
| 03-10 Blood on the Handle	| 88	| 1.98	| arboreal |
| 03-12 Stock Car Champion	| 89	| 2.02	| arboreal |
| 03-25 Chinese Dragons	| 90	| 1.98	| linear |
| 03- 27 Smoke Jumper	| 88	| 1.98	| linear |
| 03-31 Island of Time	| 89	| 1.98	| linear |
| 03-37 Behind the Wheel	| 87	| 1.98	| linear |
| 03-39 SIlver Wings	| 86	| 2	| arboreal |
| 03-55 Motocross Mania	| 90	| 2.02	| arboreal |
| 03-59 Project UFO	| 90	| 2.02	| arboreal |
| 04-05 Last Run	| 92	| 2.17	| linear |
| 04-11 Tattoo of Death	| 92	| 1.98	| arboreal |
| 04-12 Possessed!	| 96	| 1.98	| arboreal |
| 04-22 Death in the Dorm	| 91	| 2	| linear |
| 04-29 Killer Virus	| 90	| 1.98	| arboreal |
| 42- 36 Haunted House	| 46	| 1.96	| arboreal |
| 42-37 Your Very Own Robot	| 46	| 1.96	| arboreal |

| EDWARD PACKARD	| Nodes	| Average Degree	| General Shape |
|-----------------------|-------|-------|-------|
| 04-02 Who Are You?	| 95	| 1.98	| arboreal |
| 04-04 War with the Mutant Spider Ants	| 97	| 2	| linear |
| 04-06 Cyberspace Warrior	| 93	| 1.98	| linear |
| 04-08 You are an Alien	| 95	| 2.02	| linear |
| 04-10 Sky-Jam!	| 96	| 2.06	| linear |
| 04-13 Typhoon!	| 91	| 2.07	| arboreal |
| 04-15 Fright Night	| 93	| 2.09	| arboreal |
| 04-19 Hostage!	| 100	| 1.98	| linear |
| 04-21 Greed, Guns, and Gold	| 95	| 2	| linear |
| 04-23 Mountain Biker	| 92	| 2	| arboreal |
| 04-25 Power Dome	| 93	| 1.98	| linear |
| 04-33 Fire on Ice	| 92	| 2.02	| arboreal |
| 04-34 Fugitive	| 92	| 2	| arboreal |
| 04-70 Computer Takeover	| 100	| 2.02	| linear |
| 11-11 Tenopia Island	| 108	| 5.83	| web-like |
| 11-15 The Castle of Frome	| 106	| 3.43	| web-like |

### Similarities

In the Choose Your Own Adventure samples’ graphs, as well as the rest of the series books’ graphs the shape of the graphs were not indicative enough of the book’s author. As I collected the data from each of the sample books, I realize that the series’ structure was more prominent than the authorship. The books within my sampling were in the 85-110 node range and had an average node degree of 2.01. Both authors’ books had a variety of linear and arboreal graphs. This implies that neither of them preferred a specific narrative structure when composing the books and inputing narrative choices.

#### Montgomery: CYOA

{% include graph-set.html imagelist=page.topics.montgomery-cyoa.images scale="1" %}

#### Packard: CYOA

{% include graph-set.html imagelist=page.topics.packard-cyoa.images scale="1" %}

### Differences and Conclusions

When I looked at the samples outside of the Choose Your Own Adventure series I was able to see more prominent differences. These difference were not as indicative of the authors themselves, rather the series they were writing in.

#### Montgomery: Dragonlarks

{% include graph-set.html imagelist=page.topics.montgomery-cyoa-dragonlarks.images scale="1" %}

The Choose Your Own Adventure: Dragonlarks series is a spin-off series for younger readers to read before bed. When I analyzed the data from these two samples of Montgomery’s books, I saw about half as many nodes as in a regular series and an average node degree that was about the same or less. Since these books are shorter their graphs were more arboreal than linear.

#### Packard: Other

{% include graph-set.html imagelist=page.topics.packard-other.images scale="1" %}

The Escape from Tenopia series features one book from Packard, which is homogenous with the rest of the series. Like the Escape from Tenopia series, the Escape from the Kingdom of Frome series also follows similar structure. These samples’ graphs were both web-like and had much higher average node degrees even though they both had around 105 nodes. *Tenopia Island* had an average node degree of 5.83 and *The Castle of Frome* had an average node degree of 3.43.

Across these series, I found it very interesting that the structures used somewhat overshadowed the individual books’ authorship. Both Edward Packard and R.A. Montgomery were able to adjust their writing style and narrative structure according to the gamebook series they were writing in.

----------
