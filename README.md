# WWDC Session Dataset 

## Why? :bulb:

Because, who doesn't like scraping!? 

I built the dataset because I found out that a lot of applications/utilities that deal with WWDC session data, often get broken when Apple updates their websites and links. That's still going to keep happening, but now those apps can point to the relevant dataset files and the community can keep those up-to-date. 

The code used to build the dataset is also available so that it can be kept updated.

## Format :page_facing_up:

```JSON
{
    "title" : "Building Concurrent User Interfaces on iOS",
    "year" : "2012",
    "code" : "211",
    "abstract" : "For a great user experience, it's essential to keep your applications... without blocking user interaction.",
    "tags" : ["iOS"],
    "sd_video" : "http://developer.apple.com/video_sd.mp4",
    "hd_video" : "http://developer.apple.com/video_hd.mp4",
    "slides" : "http://developer.apple.com/slides.pdf",
    "transcript" : [{start: 84.0, end: 86.0, text: "Devices are great"}, ..., {{start: 3000.0, end: 3001.0, text: "The end"}}]
}
```

Because the transcripts are quite heavy, two versions of the dataset are provided, one with transcripts and one with an empty array of transcripts.

| Year  | Size (no transcripts) | Size (with transcripts) | JSON (no transcripts)            | JSON (transcripts)
| ----- | --------------------- | ----------------------- | -------------------------------- | -----------------------------------------
| 2010  |                       |                         |                                  |
| 2011  |       `98 KB`         |                         | [2011](./datasets/wwdc2011.json) | 
| 2012  |       `99 KB`         |                         | [2012](./datasets/wwdc2012.json) | 
| 2013  |       `73 KB`         |                         | [2013](./datasets/wwdc2013.json) | 
| 2014  |       `83 KB`         |                         | [2014](./datasets/wwdc2014.json) | 
| 2015  |       `85 KB`         |        `7.7 MB`         | [2015](./datasets/wwdc2015.json) | [2015](./datasets/wwdc2015_transcript.json)

Note: 

## Contributing :construction_worker:

### What's missing

* Session data for WWDC 2010 sits behind Apple's developer website (non-public).
* Transcripts from 2010-2014 (they are not in Apple's Website).
* Maybe I can look at [ASCII WWDC](https://github.com/ASCIIwwdc/asciiwwdc.com) to import some of those transcripts to the same format that Apple used for 2015.

### How the scraper works

Be sure to install [scrapy](http://scrapy.org)

```
pip install scrapy
```

Then, from the project folder just execute the build script (it's a Python script)

```bash
./build
```

That should output several `.json` files in your current working directory.

### Contact

For questions, ideas and/or trolling, I'm on Twitter :grin:

<img src="https://cdn3.iconfinder.com/data/icons/free-social-icons/67/twitter_circle_black-512.png" alt="Twitter logo" height="17" > [http://twitter.com/ngoles](http://twitter.com/ngoles)

## Copyright

All content copyright © 2010–2016 Apple Inc. All rights reserved.
