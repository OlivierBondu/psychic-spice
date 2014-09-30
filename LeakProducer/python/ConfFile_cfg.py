import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( 50 ) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 5 )

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
    ignoreTotal = cms.untracked.int32(1),
    monitorPssAndPrivate = cms.untracked.bool(False)
    )


process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        '/store/cmst3/user/gpetrucc/miniAOD/v1/GluGluToHToGG_M-125_13TeV-powheg-pythia6_Flat20to50_PAT.root'
    )
)

process.myProducerLabel = cms.EDProducer('LeakProducer',
    PFCandidatesTag=cms.untracked.InputTag('packedPFCandidates'),
    VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices'),
    UseEachTrackOnce=cms.untracked.bool(False),
    MaxAllowedDz=cms.double(0.2) # in cm
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
