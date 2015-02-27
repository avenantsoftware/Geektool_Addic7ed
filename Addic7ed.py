#!/usr/bin/python
# encoding: utf-8

import feedparser

feed = feedparser.parse('http://www.addic7ed.com/rss.php?mode=hotspot')

// enter all series you folow here:
keywords = ['Seriename1','Seriename2','Seriename3']

// This is to also show when a new series starts
keywords2 = ['01x01']

tmp = []

for entry in feed['entries']:
  if tmp.__contains__(entry.title): 
    continue
  else:
    tmp.append(entry.title)
    if any(word in entry.title for word in keywords):
      print entry.title
    if any(word in entry.title for word in keywords2):
      print "New Serie: " + entry.title
    if not tmp:
      print "No new subtitles found"
