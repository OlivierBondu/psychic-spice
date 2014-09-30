psychic-spice
=============

  * Based on an issue from https://github.com/cms-analysis/flashgg
  * HN thread : https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/150/1/1.html

1. Create a CMSSW_7_0_7_patch1 project:
 ```
 # make sure you are on lxplus6 or otherwise using an SLC6 machine
 # make sure SCRAM_ARCH is slc6_amd64_gcc481 (should be default)
 cmsrel CMSSW_7_0_7_patch1
 cd CMSSW_7_0_7_patch1/src
 cmsenv
 ```
 
2. Run the simple leaky producer 
 ```
 cd $CMSSW_BASE/src
 git clone https://github.com/OlivierBondu/psychic-spice.git
 scram b -j 4
 cd psychic-spice
 cmsRun LeakProducer/python/ConfFile_cfg.py
 ```
