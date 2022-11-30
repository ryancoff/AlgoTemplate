The problem with "low<high" is that when "low == high", it's already outside the loop.
So if you use only while loop, you can't check condition (e.g: check_condition(low) ) for this case .

P/s: Check out problem "#718. Maximum Length of Repeated Subarray"
I used "low<high" for this one, so i had to check condition after while loop.