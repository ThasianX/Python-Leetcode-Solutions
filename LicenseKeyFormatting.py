class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
      groups = [""]

      for c in filter(lambda c: c != '-', reversed(s)):
        if len(groups[-1]) == k:
          groups.append("")
        groups[-1] = c.upper() + groups[-1]

      return "-".join(groups[::-1])

        
tests = [
  (
    ("5F3Z-2e-9-w",4,),
    "5F3Z-2E9W",
  ),
  (
    ("2-5g-3-J",2,),
    "2-5G-3J",
  ),
  (
    ("--a-a-a-a--",2,),
    "AA-AA",
  ),
]