class Solution:
    def findLatestTime(self, s: str) -> str:
        hh, mm = s.split(":")

        if hh[0] == "?":
            if hh[1] == "?":
                hh = "11"
            else:
                if hh[1] >= "0" and hh[1] <= "1":
                    hh = "1" + hh[1]
                else:
                    hh = "0" + hh[1]
        elif hh[1] == "?":
            if hh[0] == "1":
                hh = hh[0] + "1"
            else:
                hh = hh[0] + "9"

        if mm[0] == "?":
            mm = "5" + mm[1] if mm[1] != "?" else "59"
        elif mm[1] == "?":
            mm = mm[0] + "9"

        return hh + ":" + mm