# WWDC Session Dataset

## Why? 💡

Because, who doesn't like scraping!? 

In reality... I built the dataset because I found out that a lot of applications/utilities that deal with WWDC Session data, often get broken when Apple updates their websites and links. That's still going to keep happening, but now those apps can point to the relevant dataset files and the community can keep those up-to-date. In that way, there's less duplicated effort and everyone wins.

Applications are varied, from educational iOS-related projects that could use some Apple related data instead of some random dataset, to actual apps that might want deal with WWDC sessions in some way or another.

## Format 📄

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

Because the transcripts are quite heavy, two versions of the dataset are provided, one with Transcripts and one with an empty array of transcripts.

| Year  | Size (no transcripts) | Size (with transcripts) | JSON (no transcripts)      | JSON (transcripts)
| ----- | --------------------- | ----------------------- | -------------------------- | ------------------------ |
| 2010  |       `? KB`          |         `? MB`          |                            |
| 2011  |       `98 KB`         |         `? MB`          | [2011](datasets/2011.json) | [2011](datasets/2011.json)
| 2012  |       `99 KB`         |         `? MB`          | [2012](datasets/2011.json) | [2012](datasets/2012.json)
| 2013  |       `73 KB`         |         `? MB`          | [2013](datasets/2011.json) | [2013](datasets/2013.json)
| 2014  |       `83 KB`         |         `? MB`          | [2014](datasets/2011.json) | [2014](datasets/2014.json)
| 2015  |       `85 KB`         |        `7.7 MB`         | [2015](datasets/2011.json) | [2015](datasets/2015.json)

## Usage 🚀

Just download the data and be creative!

## Contributing 🛠

The.


## About 😁

## Copyright

All content copyright © 2010–2016 Apple Inc. All rights reserved.
