# An Optimized Space solution -- good for production env
  * Tracking warmer/greater value in order (A-->Z) (1-->N)
    * Initialize an integer to track the hottest/greatest
    * Iterate backwards through the input, check if the current day is the hottest/greatest one seen so far.
      * If it is, update hottest and move on. 
      * Otherwise, do following:
        * Initialize a variable `days=1` because next answer must be at least `one day in the future` or `+1 position in order`
        * while `temperatures[currDay + days] <= temperatures[currDay]`:
          * Add `answer[currDay + days]` to `days`. This effectively jumps directly to the next wamer day/ position to check.
          * Set `answer[currDay] = days`
