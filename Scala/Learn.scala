object main {
  def main(args: Array[String]): Unit = {
    val courseMap = Map[Int, String]()
    courseMap += (1 -> "Scala")
    courseMap += (2 -> "Java")
    courseMap += (3 -> "Python")
    courseMap += (4 -> "C++")

    val key = for (key <- courseMap.keys) yield(key)
    // prints as set because keys are unique
    println(key)

    val value = for (value <- courseMap.values) yield(value)
    // prints as list because values can be duplicate
    println(value)

    val swapmap = for ((key, value) <- courseMap) yield (value, key)
    // prints as map because keys are unique
    println(swapmap)
  }
}

