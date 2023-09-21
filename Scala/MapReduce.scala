import scala.collection.mutable.Map

object Main {
  def main(args: Array[String]): Unit = {
    val wordMap = Map[Int, String]()
    var count =0
    val in = new java.util.Scanner(new java.io.File("myFile.txt"))
    while (in.hasNext()) {
        count=count+1
        wordMap+=(count->in.next())
    }
    print(wordMap)
  }
}