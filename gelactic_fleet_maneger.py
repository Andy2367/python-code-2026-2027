class spaceship:
    def __init__(self, name , nfule, wfule , fbr, norm_dist, warp_dist):
        self.name = name
        self.nfule = nfule
        self.wfule = wfule
        self.fbr = fbr
        self.norm_dist = norm_dist
        self.warp_dist = warp_dist
    def travel_norm(self):
        print("traveling")
        self.nfule = self.nfule - (self.fbr * self.norm_dist)
        return print(f"{self.nfule} units of normal fule remaneing")
    def travel_warp(self):
        self.wfule = self.wfule -(self.fbr * self.warp_dist)
        return print(f"{self.wfule} units of warp fule remaneing")

class fighter(spaceship):
    def __init__(self, name, nfule, wfule, fbr, norm_dist, warp_dist):
        super().__init__(name, nfule, wfule, fbr, norm_dist, warp_dist)
    def travel_norm(self): # add rest of func