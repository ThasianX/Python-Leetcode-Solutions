from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
      def getStrippedAddress(email: str) -> str:
        local_name = ""
        i = 0

        # Construct local name
        while i < len(email):
          c = email[i]
          if c == '@' or c =='+':
            break
          if c != '.':
            local_name += c

          i += 1

        # Shift i to the index of '@', if it's already not
        while email[i] != '@':
          i += 1
          
        return local_name + email[i:]
      
      uniqueAddresses = set()

      for email in emails:
        address = getStrippedAddress(email)
        uniqueAddresses.add(address)
      
      return len(uniqueAddresses)
        
tests = [
  (
    (["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],),
    2,
  ),
  (
    (["a@leetcode.com","b@leetcode.com","c@leetcode.com"],),
    3,
  ),
]