import scala.collection.mutable.Map

object Main {

  def main(args: Array[String]): Unit = {
    val wordMap = Map[Int, String]()
    var count = 0
    val in = new java.util.Scanner(new java.io.File("myfile.txt"))
    while (in.hasNext()) {
      count = count + 1
      wordMap += (count -> in.next())
    }
    println("Word Map:")
    println(wordMap)
    println()
    countWords(wordMap)
    frequentWord(wordMap)
  }

  def countWords(wordMap: Map[Int, String]): Unit = {
    // .size returns the number of elements in the map.
    val count = wordMap.size
    println(s"Total number of words: $count")
  }

  def frequentWord(wordMap: Map[Int, String]): Unit = {
    // .values returns a collection of the values in the map.
    val allWords = wordMap.values
    // Create a map to store the word count.
    val wordCount = Map[String, Int]().withDefaultValue(0)
    
    // Iterate over the words and update the word count map.
    allWords.foreach { word =>
      wordCount(word) += 1
    }

    // Find the maximum count.
    val maxCount = wordCount.values.max

    // Find words with the maximum count.
    val mostFrequentWords = wordCount.filter { case (_, count) => count == maxCount }.keys.toList

    println(s"The most frequent word(s) with $maxCount occurrences: ${mostFrequentWords.mkString(", ")}")
}
}