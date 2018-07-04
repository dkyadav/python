#!/usr/bin/python3

import xml.sax

import time
start_time = time.time()

movies = {}

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""
      self.nodes = 0
      self.curTitle = ''
      self.moviedict = {}
      self.is_movie_block = False
   
   def getNodes(self):
      return self.nodes

   def getMovieDic(self):
      return self.moviedict

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print ("*****Movie*****")
         title = attributes["title"]
         self.curTitle = title
         self.nodes = self.nodes + 1

         #new stuff
         if title != '':
            self.moviedict[title] = {}
            self.is_movie_block = title
            print('TITLE::::'+title)
         else:
            self.is_movie_block = False


   def endDocument(self):
      print('endDocument')

         

   # Call when an elements ends
   def endElement(self, tag):
      print('herestat:'+self.CurrentData+':Tag:'+tag)

      if self.CurrentData == "type":
         print ("Type:", self.type)
      elif self.CurrentData == "format":
         print ("Format:", self.format)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "rating":
         print ("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print ("Stars:", self.stars)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      
      #print('here')
      #new stuff
      
      # if tag == 'movie':
      #    self.is_movie_block = False
      #    print('here:'+self.CurrentData)

      #oldstuff
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content

      curDict = {}
      curDict['type'] = self.type
      curDict['format'] = self.format
      curDict['year'] = self.year
      curDict['rating'] = self.rating
      curDict['stars'] = self.stars
      curDict['description'] = self.description
      
      if self.curTitle != '':
         movies.update({self.curTitle : curDict })

      #and self.is_movie_block != 'movie'
      print('CHECK FLAG:::'+str(self.is_movie_block))

      if self.is_movie_block:
         if self.CurrentData in self.moviedict[self.is_movie_block]:
            self.moviedict[self.is_movie_block][self.CurrentData] += content.strip()
         else:
            self.moviedict[self.is_movie_block][self.CurrentData] = content.strip()
      
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   #parser.parse("moviesbig.xml")
   parser.parse("movies.xml")

   print('Total number of nodes: ' + str(Handler.getNodes()))
   print("--- %s Total seconds ---" % (time.time() - start_time))
   print(movies)
   print('-------')
   print(Handler.getMovieDic())