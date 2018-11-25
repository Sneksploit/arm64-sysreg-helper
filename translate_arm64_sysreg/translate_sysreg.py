import sys


def translate_sysinst(op0, op1, CRm, CRn, op2):

	if op0 == 3:
		if op1 == 1:
			if CRm == 0:
				if CRn == 0:
					if op2 == 1:
						return("CLIDR_EL1", "Level ID Register")
					if op2 == 0:
						return("CCSIDR_EL1", "Cache Size ID Register	Provides information about the architecture of the currently selected cache. See Cache discovery")
					if op2 == 2:
						return("CCSIDR2_EL1", "Cache Size ID Register	Provides information about the architecture of the currently selected cache. See Cache discovery")
					if op2 == 7:
						return("AIDR_EL1", "")
		if op1 == 0:
			if CRm == 10:
				if CRn == 3:
					if op2 == 0:
						return("AMAIR_EL1", "")
				if CRn == 2:
					if op2 == 0:
						return("MAIR_EL1", "Attribute Indirection Register	Provides the memory attribute encodings corresponding to the possible values in a Long-descriptor format translation table entry for stage 1 translations at ELn. See Memory types")
				if CRn == 4:
					if op2 == 1:
						return("LOREA_EL1", "")
					if op2 == 0:
						return("LORSA_EL1", "")
					if op2 == 3:
						return("LORC_EL1", "")
					if op2 == 2:
						return("LORN_EL1", "")
					if op2 == 7:
						return("LORID_EL1", "")
			if CRm == 13:
				if CRn == 0:
					if op2 == 1:
						return("CONTEXTIDR_EL1", "")
					if op2 == 4:
						return("TPIDR_EL1", "Read/Write Thread ID Register	Provides a location where software executing at ELn can store thread identifying information, for OS management purposes. See Context switching")
			if CRm == 12:
				if CRn == 11:
					if op2 == 1:
						return("(ICC/ICV)_DIR_EL1", "")
					if op2 == 3:
						return("(ICC/ICV)_RPR_EL1", "")
					if op2 == 5:
						return("ICC_SGI1R_EL1", "")
					if op2 == 7:
						return("ICC_SGI0R_EL1", "")
					if op2 == 6:
						return("ICC_ASGI1R_EL1", "")
				if CRn == 12:
					if op2 == 1:
						return("(ICC/ICV)_EOIR1_EL1", "")
					if op2 == 0:
						return("(ICC/ICV)_IAR1_EL1", "")
					if op2 == 3:
						return("(ICC/ICV)_BPR1_EL1", "")
					if op2 == 2:
						return("(ICC/ICV)_HPPIR1_EL1", "")
					if op2 == 5:
						return("ICC_SRE_EL1", "")
					if op2 == 4:
						return("(ICC/ICV)_CTLR_EL1", "")
					if op2 == 7:
						return("(ICC/ICV)_IGRPEN1_EL1", "")
					if op2 == 6:
						return("(ICC/ICV)_IGRPEN0_EL1", "")
				if CRn == 1:
					if op2 == 1:
						return("DISR_EL1", "")
					if op2 == 0:
						return("ISR_EL1", "")
				if CRn == 0:
					if op2 == 1:
						return("RVBAR_EL1", "")
					if op2 == 0:
						return("VBAR_EL1", "Based Address Register	Holds the exception base address for any exception that is taken to ELn. See AArch64 exception table")
					if op2 == 2:
						return("RMR_EL1", "")
				if CRn == 9:
					if op2 == 1:
						return("(ICC/ICV)_AP1R1_EL1", "")
					if op2 == 0:
						return("(ICC/ICV)_AP1R0_EL1", "")
					if op2 == 3:
						return("(ICC/ICV)_AP1R3_EL1", "")
					if op2 == 2:
						return("(ICC/ICV)_AP1R2_EL1", "")
				if CRn == 8:
					if op2 == 1:
						return("(ICC/ICV)_EOIR0_EL1", "")
					if op2 == 0:
						return("(ICC/ICV)_IAR0_EL1", "")
					if op2 == 3:
						return("(ICC/ICV)_BPR0_EL1", "")
					if op2 == 2:
						return("(ICC/ICV)_HPPIR0_EL1", "")
					if op2 == 5:
						return("(ICC/ICV)_AP0R1_EL1", "")
					if op2 == 4:
						return("(ICC/ICV)_AP0R0_EL1", "")
					if op2 == 7:
						return("(ICC/ICV)_AP0R3_EL1", "")
					if op2 == 6:
						return("(ICC/ICV)_AP0R2_EL1", "")
			if CRm == 14:
				if CRn == 1:
					if op2 == 0:
						return("CNTKCTL_EL1", "Kernel Control Register	Controls the generation of an event stream from the virtual counter. Also controls access from EL0 to the physical counter, virtual counter, EL1 physical timers, and the virtual timer. See Timers")
			if CRm == 1:
				if CRn == 0:
					if op2 == 1:
						return("ACTLR_EL1", "Control Register	Controls processor-specific features")
					if op2 == 0:
						return("SCTLR_EL1", "Control Register	Controls architectural features, for example the MMU, caches and alignment checking")
					if op2 == 2:
						return("CPACR_EL1", "Access Control Register	Controls access to Trace, floating-point, and NEON functionality. See ISB in more detail")
				if CRn == 2:
					if op2 == 1:
						return("TRFCR_EL1", "")
					if op2 == 0:
						return("ZCR_EL1", "")
			if CRm == 0:
				if CRn == 1:
					if op2 == 1:
						return("ID_PFR1_EL1", "")
					if op2 == 0:
						return("ID_ISAR0_EL1", "")
					if op2 == 3:
						return("ID_AFR0_EL1", "")
					if op2 == 2:
						return("ID_DFR0_EL1", "")
					if op2 == 5:
						return("ID_MMFR1_EL1", "")
					if op2 == 4:
						return("ID_MMFR0_EL1", "")
					if op2 == 7:
						return("ID_MMFR3_EL1", "")
					if op2 == 6:
						return("ID_MMFR2_EL1", "")
				if CRn == 0:
					if op2 == 0:
						return("MIDR_EL1", "ID Register	The type of processor the code is running on (part number and revision)")
					if op2 == 5:
						return("MPIDR_EL1", "Affinity Register	The processor and cluster IDs, in multi-core or cluster systems. See Determining which core the code is running on")
					if op2 == 6:
						return("REVIDR_EL1", "")
				if CRn == 3:
					if op2 == 1:
						return("MVFR1_EL1", "")
					if op2 == 0:
						return("MVFR0_EL1", "")
					if op2 == 2:
						return("MVFR2_EL1", "")
					if op2 == 4:
						return("ID_PFR2_EL1", "")
				if CRn == 2:
					if op2 == 1:
						return("ID_ISAR1_EL1", "")
					if op2 == 3:
						return("ID_ISAR3_EL1", "")
					if op2 == 2:
						return("ID_ISAR2_EL1", "")
					if op2 == 5:
						return("ID_ISAR5_EL1", "")
					if op2 == 4:
						return("ID_ISAR4_EL1", "")
					if op2 == 6:
						return("ID_MMFR4_EL1", "")
				if CRn == 5:
					if op2 == 1:
						return("ID_AA64DFR1_EL1", "")
					if op2 == 0:
						return("ID_AA64DFR0_EL1", "")
					if op2 == 5:
						return("ID_AA64AFR1_EL1", "")
					if op2 == 4:
						return("ID_AA64AFR0_EL1", "")
				if CRn == 4:
					if op2 == 1:
						return("ID_AA64PFR1_EL1", "")
					if op2 == 0:
						return("ID_AA64PFR0_EL1", "")
					if op2 == 2:
						return("ID_AA64ZFR0_EL1", "")
				if CRn == 7:
					if op2 == 1:
						return("ID_AA64MMFR1_EL1", "")
					if op2 == 0:
						return("ID_AA64MMFR0_EL1", "")
					if op2 == 2:
						return("ID_AA64MMFR2_EL1", "")
				if CRn == 6:
					if op2 == 1:
						return("ID_AA64ISAR1_EL1", "")
					if op2 == 0:
						return("ID_AA64ISAR0_EL1", "")
			if CRm == 2:
				if CRn == 1:
					if op2 == 1:
						return("APIAKeyHi_EL1", "")
					if op2 == 0:
						return("APIAKeyLo_EL1", "")
					if op2 == 3:
						return("APIBKeyHi_EL1", "")
					if op2 == 2:
						return("APIBKeyLo_EL1", "")
				if CRn == 0:
					if op2 == 1:
						return("TTBR1_EL1", "Table Base Register 1	Holds the base address of translation table 1, and information about the memory it occupies. This is one of the translation tables for the stage 1 translation of memory accesses at EL0 and EL1. See Separation of kernel and application Virtual Address spaces")
					if op2 == 0:
						return("TTBR0_EL1", "Table Base Register 1	Holds the base address of translation table 1, and information about the memory it occupies. This is one of the translation tables for the stage 1 translation of memory accesses at EL0 and EL1. See Separation of kernel and application Virtual Address spaces")
					if op2 == 2:
						return("TCR_EL1", "Control Register	Determines which of the Translation Table Base Registers define the base address for a translation table walk required for the stage 1 translation of a memory access from ELn. Also controls the translation table format and holds cacheability and shareability information. See Separation of kernel and application Virtual Address spaces")
				if CRn == 3:
					if op2 == 1:
						return("APGAKeyHi_EL1", "")
					if op2 == 0:
						return("APGAKeyLo_EL1", "")
				if CRn == 2:
					if op2 == 1:
						return("APDAKeyHi_EL1", "")
					if op2 == 0:
						return("APDAKeyLo_EL1", "")
					if op2 == 3:
						return("APDBKeyHi_EL1", "")
					if op2 == 2:
						return("APDBKeyLo_EL1", "")
			if CRm == 5:
				if CRn == 1:
					if op2 == 1:
						return("AFSR1_EL1", "")
					if op2 == 0:
						return("AFSR0_EL1", "")
				if CRn == 3:
					if op2 == 1:
						return("ERRSELR_EL1", "")
					if op2 == 0:
						return("ERRIDR_EL1", "")
				if CRn == 2:
					if op2 == 0:
						return("ESR_EL1", "Syndrome Register	Includes information about the reasons for the exception. See The Exception Syndrome Register")
				if CRn == 5:
					if op2 == 1:
						return("ERXMISC1_EL1", "")
					if op2 == 0:
						return("ERXMISC0_EL1", "")
					if op2 == 3:
						return("ERXMISC3_EL1", "")
					if op2 == 2:
						return("ERXMISC2_EL1", "")
				if CRn == 4:
					if op2 == 1:
						return("ERXCTLR_EL1", "")
					if op2 == 0:
						return("ERXFR_EL1", "")
					if op2 == 3:
						return("ERXADDR_EL1", "")
					if op2 == 2:
						return("ERXSTATUS_EL1", "")
					if op2 == 5:
						return("ERXPFGCTL_EL1", "")
					if op2 == 4:
						return("ERXPFGF_EL1", "")
					if op2 == 6:
						return("ERXPFGCDN_EL1", "")
			if CRm == 4:
				if CRn == 1:
					if op2 == 0:
						return("SP_EL0", "")
				if CRn == 0:
					if op2 == 1:
						return("ELR_EL1", "Link Register	Holds the address of the instruction which caused the exception")
					if op2 == 0:
						return("SPSR_EL1", "Program Status Register	Holds the saved processor state when an exception is taken to this mode or Exception level")
				if CRn == 2:
					if op2 == 0:
						return("SPSel", "")
					if op2 == 3:
						return("PAN", "")
					if op2 == 2:
						return("CurrentEL", "")
					if op2 == 4:
						return("UAO", "")
				if CRn == 6:
					if op2 == 0:
						return("(ICC/ICV)_PMR_EL1", "")
			if CRm == 7:
				if CRn == 4:
					if op2 == 0:
						return("PAR_EL1", "")
			if CRm == 6:
				if CRn == 0:
					if op2 == 0:
						return("FAR_EL1", "Address Register	Holds the virtual faulting address. See Handling synchronous exceptions")
			if CRm == 9:
				if CRn == 9:
					if op2 == 0:
						return("PMSCR_EL1", "")
					if op2 == 3:
						return("PMSIRR_EL1", "")
					if op2 == 2:
						return("PMSICR_EL1", "")
					if op2 == 5:
						return("PMSEVFR_EL1", "")
					if op2 == 4:
						return("PMSFCR_EL1", "")
					if op2 == 7:
						return("PMSIDR_EL1", "")
					if op2 == 6:
						return("PMSLATFR_EL1", "")
				if CRn == 10:
					if op2 == 1:
						return("PMBPTR_EL1", "")
					if op2 == 0:
						return("PMBLIMITR_EL1", "")
					if op2 == 3:
						return("PMBSR_EL1", "")
					if op2 == 7:
						return("PMBIDR_EL1", "")
				if CRn == 14:
					if op2 == 1:
						return("PMINTENSET_EL1", "")
					if op2 == 2:
						return("PMINTENCLR_EL1", "")
					if op2 == 6:
						return("PMMIR_EL1", "")
		if op1 == 3:
			if CRm == 9:
				if CRn == 13:
					if op2 == 1:
						return("PMXEVTYPER_EL0", "")
					if op2 == 0:
						return("PMCCNTR_EL0", "")
					if op2 == 2:
						return("PMXEVCNTR_EL0", "")
				if CRn == 12:
					if op2 == 1:
						return("PMCNTENSET_EL0", "")
					if op2 == 0:
						return("PMCR_EL0", "")
					if op2 == 3:
						return("PMOVSCLR_EL0", "")
					if op2 == 2:
						return("PMCNTENCLR_EL0", "")
					if op2 == 5:
						return("PMSELR_EL0", "")
					if op2 == 4:
						return("PMSWINC_EL0", "")
					if op2 == 7:
						return("PMCEID1_EL0", "")
					if op2 == 6:
						return("PMCEID0_EL0", "")
				if CRn == 14:
					if op2 == 0:
						return("PMUSERENR_EL0", "")
					if op2 == 3:
						return("PMOVSSET_EL0", "")
			if CRm == 0:
				if CRn == 0:
					if op2 == 0:
						return("CTR_EL0", "Type Register	Information about the architecture of the integrated caches. See Cache discovery")
					if op2 == 7:
						return("DCZID_EL0", "Cache Zero ID Register	Indicates the block size written with byte values of 0 by the Data Cache Zero by Virtual Address (DCZVA) system instruction. See Cache discovery")
			if CRm == 13:
				if CRn == 13:
					if op2 == 1:
						return("AMEVCNTR19_EL0", "")
					if op2 == 0:
						return("AMEVCNTR18_EL0", "")
					if op2 == 3:
						return("AMEVCNTR111_EL0", "")
					if op2 == 2:
						return("AMEVCNTR110_EL0", "")
					if op2 == 5:
						return("AMEVCNTR113_EL0", "")
					if op2 == 4:
						return("AMEVCNTR112_EL0", "")
					if op2 == 7:
						return("AMEVCNTR115_EL0", "")
					if op2 == 6:
						return("AMEVCNTR114_EL0", "")
				if CRn == 12:
					if op2 == 1:
						return("AMEVCNTR11_EL0", "")
					if op2 == 0:
						return("AMEVCNTR10_EL0", "")
					if op2 == 3:
						return("AMEVCNTR13_EL0", "")
					if op2 == 2:
						return("AMEVCNTR12_EL0", "")
					if op2 == 5:
						return("AMEVCNTR15_EL0", "")
					if op2 == 4:
						return("AMEVCNTR14_EL0", "")
					if op2 == 7:
						return("AMEVCNTR17_EL0", "")
					if op2 == 6:
						return("AMEVCNTR16_EL0", "")
				if CRn == 15:
					if op2 == 1:
						return("AMEVTYPER19_EL0", "")
					if op2 == 0:
						return("AMEVTYPER18_EL0", "")
					if op2 == 3:
						return("AMEVTYPER111_EL0", "")
					if op2 == 2:
						return("AMEVTYPER110_EL0", "")
					if op2 == 5:
						return("AMEVTYPER113_EL0", "")
					if op2 == 4:
						return("AMEVTYPER112_EL0", "")
					if op2 == 7:
						return("AMEVTYPER115_EL0", "")
					if op2 == 6:
						return("AMEVTYPER114_EL0", "")
				if CRn == 14:
					if op2 == 1:
						return("AMEVTYPER11_EL0", "")
					if op2 == 0:
						return("AMEVTYPER10_EL0", "")
					if op2 == 3:
						return("AMEVTYPER13_EL0", "")
					if op2 == 2:
						return("AMEVTYPER12_EL0", "")
					if op2 == 5:
						return("AMEVTYPER15_EL0", "")
					if op2 == 4:
						return("AMEVTYPER14_EL0", "")
					if op2 == 7:
						return("AMEVTYPER17_EL0", "")
					if op2 == 6:
						return("AMEVTYPER16_EL0", "")
				if CRn == 0:
					if op2 == 3:
						return("TPIDRRO_EL0", "Read-Only Thread ID Register	Provides a location where software executing at EL1 or higher can store thread identifying information. This informaton is visible to software executing at EL0, for OS management purposes. See Context switching")
					if op2 == 2:
						return("TPIDR_EL0", "Read/Write Thread ID Register	Provides a location where software executing at ELn can store thread identifying information, for OS management purposes. See Context switching")
				if CRn == 3:
					if op2 == 1:
						return("AMCNTENSET1_EL0", "")
					if op2 == 0:
						return("AMCNTENCLR1_EL0", "")
				if CRn == 2:
					if op2 == 1:
						return("AMCFGR_EL0", "")
					if op2 == 0:
						return("AMCR_EL0", "")
					if op2 == 3:
						return("AMUSERENR_EL0", "")
					if op2 == 2:
						return("AMCGCR_EL0", "")
					if op2 == 5:
						return("AMCNTENSET0_EL0", "")
					if op2 == 4:
						return("AMCNTENCLR0_EL0", "")
				if CRn == 5:
					if op2 == 1:
						return("AMEVCNTR09_EL0", "")
					if op2 == 0:
						return("AMEVCNTR08_EL0", "")
					if op2 == 3:
						return("AMEVCNTR011_EL0", "")
					if op2 == 2:
						return("AMEVCNTR010_EL0", "")
					if op2 == 5:
						return("AMEVCNTR013_EL0", "")
					if op2 == 4:
						return("AMEVCNTR012_EL0", "")
					if op2 == 7:
						return("AMEVCNTR015_EL0", "")
					if op2 == 6:
						return("AMEVCNTR014_EL0", "")
				if CRn == 4:
					if op2 == 1:
						return("AMEVCNTR01_EL0", "")
					if op2 == 0:
						return("AMEVCNTR00_EL0", "")
					if op2 == 3:
						return("AMEVCNTR03_EL0", "")
					if op2 == 2:
						return("AMEVCNTR02_EL0", "")
					if op2 == 5:
						return("AMEVCNTR05_EL0", "")
					if op2 == 4:
						return("AMEVCNTR04_EL0", "")
					if op2 == 7:
						return("AMEVCNTR07_EL0", "")
					if op2 == 6:
						return("AMEVCNTR06_EL0", "")
				if CRn == 7:
					if op2 == 1:
						return("AMEVTYPER09_EL0", "")
					if op2 == 0:
						return("AMEVTYPER08_EL0", "")
					if op2 == 3:
						return("AMEVTYPER011_EL0", "")
					if op2 == 2:
						return("AMEVTYPER010_EL0", "")
					if op2 == 5:
						return("AMEVTYPER013_EL0", "")
					if op2 == 4:
						return("AMEVTYPER012_EL0", "")
					if op2 == 7:
						return("AMEVTYPER015_EL0", "")
					if op2 == 6:
						return("AMEVTYPER014_EL0", "")
				if CRn == 6:
					if op2 == 1:
						return("AMEVTYPER01_EL0", "")
					if op2 == 0:
						return("AMEVTYPER00_EL0", "")
					if op2 == 3:
						return("AMEVTYPER03_EL0", "")
					if op2 == 2:
						return("AMEVTYPER02_EL0", "")
					if op2 == 5:
						return("AMEVTYPER05_EL0", "")
					if op2 == 4:
						return("AMEVTYPER04_EL0", "")
					if op2 == 7:
						return("AMEVTYPER07_EL0", "")
					if op2 == 6:
						return("AMEVTYPER06_EL0", "")
			if CRm == 14:
				if CRn == 10:
					if op2 == 1:
						return("PMEVCNTR17_EL0", "")
					if op2 == 0:
						return("PMEVCNTR16_EL0", "")
					if op2 == 3:
						return("PMEVCNTR19_EL0", "")
					if op2 == 2:
						return("PMEVCNTR18_EL0", "")
					if op2 == 5:
						return("PMEVCNTR21_EL0", "")
					if op2 == 4:
						return("PMEVCNTR20_EL0", "")
					if op2 == 7:
						return("PMEVCNTR23_EL0", "")
					if op2 == 6:
						return("PMEVCNTR22_EL0", "")
				if CRn == 13:
					if op2 == 1:
						return("PMEVTYPER9_EL0", "")
					if op2 == 0:
						return("PMEVTYPER8_EL0", "")
					if op2 == 3:
						return("PMEVTYPER11_EL0", "")
					if op2 == 2:
						return("PMEVTYPER10_EL0", "")
					if op2 == 5:
						return("PMEVTYPER13_EL0", "")
					if op2 == 4:
						return("PMEVTYPER12_EL0", "")
					if op2 == 7:
						return("PMEVTYPER15_EL0", "")
					if op2 == 6:
						return("PMEVTYPER14_EL0", "")
				if CRn == 12:
					if op2 == 1:
						return("PMEVTYPER1_EL0", "")
					if op2 == 0:
						return("PMEVTYPER0_EL0", "")
					if op2 == 3:
						return("PMEVTYPER3_EL0", "")
					if op2 == 2:
						return("PMEVTYPER2_EL0", "")
					if op2 == 5:
						return("PMEVTYPER5_EL0", "")
					if op2 == 4:
						return("PMEVTYPER4_EL0", "")
					if op2 == 7:
						return("PMEVTYPER7_EL0", "")
					if op2 == 6:
						return("PMEVTYPER6_EL0", "")
				if CRn == 15:
					if op2 == 7:
						return("PMCCFILTR_EL0", "")
				if CRn == 14:
					if op2 == 1:
						return("PMEVTYPER17_EL0", "")
					if op2 == 0:
						return("PMEVTYPER16_EL0", "")
					if op2 == 3:
						return("PMEVTYPER19_EL0", "")
					if op2 == 2:
						return("PMEVTYPER18_EL0", "")
					if op2 == 5:
						return("PMEVTYPER21_EL0", "")
					if op2 == 4:
						return("PMEVTYPER20_EL0", "")
					if op2 == 7:
						return("PMEVTYPER23_EL0", "")
					if op2 == 6:
						return("PMEVTYPER22_EL0", "")
				if CRn == 0:
					if op2 == 1:
						return("CNTPCT_EL0", "Physical Count Register	Holds the 64-bit current count value. See Timers")
					if op2 == 0:
						return("CNTFRQ_EL0", "Frequency Register	Reports the frequency of the system timer. See Timers")
					if op2 == 2:
						return("CNTVCT_EL0", "")
				if CRn == 3:
					if op2 == 1:
						return("CNTV_CTL_EL0", "")
					if op2 == 0:
						return("CNTV_TVAL_EL0", "")
					if op2 == 2:
						return("CNTV_CVAL_EL0", "")
				if CRn == 2:
					if op2 == 1:
						return("CNTP_CTL_EL0", "Physical Control Register	Control register for the EL1 physical timer. See Timers")
					if op2 == 0:
						return("CNTP_TVAL_EL0", "Physical Control Register	Control register for the EL1 physical timer. See Timers")
					if op2 == 2:
						return("CNTP_CVAL_EL0", "Physical Control Register	Control register for the EL1 physical timer. See Timers")
				if CRn == 9:
					if op2 == 1:
						return("PMEVCNTR9_EL0", "")
					if op2 == 0:
						return("PMEVCNTR8_EL0", "")
					if op2 == 3:
						return("PMEVCNTR11_EL0", "")
					if op2 == 2:
						return("PMEVCNTR10_EL0", "")
					if op2 == 5:
						return("PMEVCNTR13_EL0", "")
					if op2 == 4:
						return("PMEVCNTR12_EL0", "")
					if op2 == 7:
						return("PMEVCNTR15_EL0", "")
					if op2 == 6:
						return("PMEVCNTR14_EL0", "")
				if CRn == 8:
					if op2 == 1:
						return("PMEVCNTR1_EL0", "")
					if op2 == 0:
						return("PMEVCNTR0_EL0", "")
					if op2 == 3:
						return("PMEVCNTR3_EL0", "")
					if op2 == 2:
						return("PMEVCNTR2_EL0", "")
					if op2 == 5:
						return("PMEVCNTR5_EL0", "")
					if op2 == 4:
						return("PMEVCNTR4_EL0", "")
					if op2 == 7:
						return("PMEVCNTR7_EL0", "")
					if op2 == 6:
						return("PMEVCNTR6_EL0", "")
			if CRm == 4:
				if CRn == 2:
					if op2 == 1:
						return("DAIF", "")
					if op2 == 0:
						return("NZCV", "")
				if CRn == 5:
					if op2 == 1:
						return("DLR_EL0", "")
					if op2 == 0:
						return("DSPSR_EL0", "")
				if CRn == 4:
					if op2 == 1:
						return("FPSR", "")
					if op2 == 0:
						return("FPCR", "")
		if op1 == 2:
			if CRm == 0:
				if CRn == 0:
					if op2 == 0:
						return("CSSELR_EL1", "Size Selection Register	Selects the current Cache Size ID Register, CCSIDR_EL1, by specifying the required cache level and the cache type, either instruction or data cache. See Cache discovery")
		if op1 == 4:
			if CRm == 10:
				if CRn == 3:
					if op2 == 0:
						return("AMAIR_EL2", "")
				if CRn == 2:
					if op2 == 0:
						return("MAIR_EL2", "Attribute Indirection Register	Provides the memory attribute encodings corresponding to the possible values in a Long-descriptor format translation table entry for stage 1 translations at ELn. See Memory types")
			if CRm == 13:
				if CRn == 0:
					if op2 == 1:
						return("CONTEXTIDR_EL2", "")
					if op2 == 2:
						return("TPIDR_EL2", "Read/Write Thread ID Register	Provides a location where software executing at ELn can store thread identifying information, for OS management purposes. See Context switching")
			if CRm == 12:
				if CRn == 11:
					if op2 == 1:
						return("ICH_VTR_EL2", "")
					if op2 == 0:
						return("ICH_HCR_EL2", "")
					if op2 == 3:
						return("ICH_EISR_EL2", "")
					if op2 == 2:
						return("ICH_MISR_EL2", "")
					if op2 == 5:
						return("ICH_ELRSR_EL2", "")
					if op2 == 7:
						return("ICH_VMCR_EL2", "")
				if CRn == 13:
					if op2 == 1:
						return("ICH_LR9_EL2", "")
					if op2 == 0:
						return("ICH_LR8_EL2", "")
					if op2 == 3:
						return("ICH_LR11_EL2", "")
					if op2 == 2:
						return("ICH_LR10_EL2", "")
					if op2 == 5:
						return("ICH_LR13_EL2", "")
					if op2 == 4:
						return("ICH_LR12_EL2", "")
					if op2 == 7:
						return("ICH_LR15_EL2", "")
					if op2 == 6:
						return("ICH_LR14_EL2", "")
				if CRn == 12:
					if op2 == 1:
						return("ICH_LR1_EL2", "")
					if op2 == 0:
						return("ICH_LR0_EL2", "")
					if op2 == 3:
						return("ICH_LR3_EL2", "")
					if op2 == 2:
						return("ICH_LR2_EL2", "")
					if op2 == 5:
						return("ICH_LR5_EL2", "")
					if op2 == 4:
						return("ICH_LR4_EL2", "")
					if op2 == 7:
						return("ICH_LR7_EL2", "")
					if op2 == 6:
						return("ICH_LR6_EL2", "")
				if CRn == 1:
					if op2 == 1:
						return("VDISR_EL2", "")
				if CRn == 0:
					if op2 == 1:
						return("RVBAR_EL2", "")
					if op2 == 0:
						return("VBAR_EL2", "Based Address Register	Holds the exception base address for any exception that is taken to ELn. See AArch64 exception table")
					if op2 == 2:
						return("RMR_EL2", "")
				if CRn == 9:
					if op2 == 1:
						return("ICH_AP1R1_EL2", "")
					if op2 == 0:
						return("ICH_AP1R0_EL2", "")
					if op2 == 3:
						return("ICH_AP1R3_EL2", "")
					if op2 == 2:
						return("ICH_AP1R2_EL2", "")
					if op2 == 5:
						return("ICC_SRE_EL2", "")
				if CRn == 8:
					if op2 == 1:
						return("ICH_AP0R1_EL2", "")
					if op2 == 0:
						return("ICH_AP0R0_EL2", "")
					if op2 == 3:
						return("ICH_AP0R3_EL2", "")
					if op2 == 2:
						return("ICH_AP0R2_EL2", "")
			if CRm == 14:
				if CRn == 1:
					if op2 == 0:
						return("CNTHCTL_EL2", "")
				if CRn == 0:
					if op2 == 3:
						return("CNTVOFF_EL2", "")
				if CRn == 3:
					if op2 == 1:
						return("CNTHV_CTL_EL2", "")
					if op2 == 0:
						return("CNTHV_TVAL_EL2", "")
					if op2 == 2:
						return("CNTHV_CVAL_EL2", "")
				if CRn == 2:
					if op2 == 1:
						return("CNTHP_CTL_EL2", "")
					if op2 == 0:
						return("CNTHP_TVAL_EL2", "")
					if op2 == 2:
						return("CNTHP_CVAL_EL2", "")
				if CRn == 5:
					if op2 == 1:
						return("CNTHPS_CTL_EL2", "")
					if op2 == 0:
						return("CNTHPS_TVAL_EL2", "")
					if op2 == 2:
						return("CNTHPS_CVAL_EL2", "")
				if CRn == 4:
					if op2 == 1:
						return("CNTHVS_CTL_EL2", "")
					if op2 == 0:
						return("CNTHVS_TVAL_EL2", "")
					if op2 == 2:
						return("CNTHVS_CVAL_EL2", "")
			if CRm == 1:
				if CRn == 1:
					if op2 == 1:
						return("MDCR_EL2", "")
					if op2 == 0:
						return("HCR_EL2", "Configuration Register	Controls virtualization settings and trapping of exceptions to EL2. See Exception handling")
					if op2 == 3:
						return("HSTR_EL2", "")
					if op2 == 2:
						return("CPTR_EL2", "")
					if op2 == 7:
						return("HACR_EL2", "")
				if CRn == 0:
					if op2 == 1:
						return("ACTLR_EL2", "Control Register	Controls processor-specific features")
					if op2 == 0:
						return("SCTLR_EL2", "Control Register	Controls architectural features, for example the MMU, caches and alignment checking")
				if CRn == 3:
					if op2 == 1:
						return("SDER32_EL2", "")
				if CRn == 2:
					if op2 == 1:
						return("TRFCR_EL2", "")
					if op2 == 0:
						return("ZCR_EL2", "")
			if CRm == 0:
				if CRn == 0:
					if op2 == 0:
						return("VPIDR_EL2", "")
					if op2 == 5:
						return("VMPIDR_EL2", "")
			if CRm == 3:
				if CRn == 0:
					if op2 == 0:
						return("DACR32_EL2", "")
			if CRm == 2:
				if CRn == 1:
					if op2 == 0:
						return("VTTBR_EL2", "Translation Table Base Register	Holds the base address of the translation table for the stage 2 translation of memory accesses from Non-secure EL0 and EL1. See Memory translation")
					if op2 == 2:
						return("VTCR_EL2", "Translation Control Register	Controls the translation table walks required for the stage 2 translation of memory accesses from Non-secure EL0 and EL1. Also holds cacheability and shareability information for the accesses. See Translations at EL2 and EL3")
				if CRn == 0:
					if op2 == 1:
						return("TCR_EL2", "Control Register	Determines which of the Translation Table Base Registers define the base address for a translation table walk required for the stage 1 translation of a memory access from ELn. Also controls the translation table format and holds cacheability and shareability information. See Separation of kernel and application Virtual Address spaces")
					if op2 == 0:
						return("TTBR0_EL2", "Table Base Register 1	Holds the base address of translation table 1, and information about the memory it occupies. This is one of the translation tables for the stage 1 translation of memory accesses at EL0 and EL1. See Separation of kernel and application Virtual Address spaces")
				if CRn == 2:
					if op2 == 0:
						return("VNCR_EL2", "")
				if CRn == 6:
					if op2 == 0:
						return("VSTTBR_EL2", "")
					if op2 == 2:
						return("VSTCR_EL2", "")
			if CRm == 5:
				if CRn == 1:
					if op2 == 1:
						return("AFSR1_EL2", "")
					if op2 == 0:
						return("AFSR0_EL2", "")
				if CRn == 0:
					if op2 == 1:
						return("IFSR32_EL2", "")
				if CRn == 3:
					if op2 == 0:
						return("FPEXC32_EL2", "")
				if CRn == 2:
					if op2 == 0:
						return("ESR_EL2", "Syndrome Register	Includes information about the reasons for the exception. See The Exception Syndrome Register")
					if op2 == 3:
						return("VSESR_EL2", "")
			if CRm == 4:
				if CRn == 1:
					if op2 == 0:
						return("SP_EL1", "")
				if CRn == 0:
					if op2 == 1:
						return("ELR_EL2", "Link Register	Holds the address of the instruction which caused the exception")
					if op2 == 0:
						return("SPSR_EL2", "Program Status Register	Holds the saved processor state when an exception is taken to this mode or Exception level")
				if CRn == 3:
					if op2 == 1:
						return("SPSR_abt", "Program Status Register	Holds the saved processor state when an exception is taken to this mode or Exception level")
					if op2 == 0:
						return("SPSR_irq", "Program Status Register	Holds the saved processor state when an exception is taken to this mode or Exception level")
					if op2 == 3:
						return("SPSR_fiq", "Program Status Register	Holds the saved processor state when an exception is taken to this mode or Exception level")
					if op2 == 2:
						return("SPSR_und", "Program Status Register	Holds the saved processor state when an exception is taken to this mode or Exception level")
			if CRm == 6:
				if CRn == 0:
					if op2 == 0:
						return("FAR_EL2", "Address Register	Holds the virtual faulting address. See Handling synchronous exceptions")
					if op2 == 4:
						return("HPFAR_EL2", "")
			if CRm == 9:
				if CRn == 9:
					if op2 == 0:
						return("PMSCR_EL2", "")
		if op1 == 7:
			if CRm == 14:
				if CRn == 2:
					if op2 == 1:
						return("CNTPS_CTL_EL1", "")
					if op2 == 0:
						return("CNTPS_TVAL_EL1", "")
					if op2 == 2:
						return("CNTPS_CVAL_EL1", "")
		if op1 == 6:
			if CRm == 10:
				if CRn == 3:
					if op2 == 0:
						return("AMAIR_EL3", "")
				if CRn == 2:
					if op2 == 0:
						return("MAIR_EL3", "Attribute Indirection Register	Provides the memory attribute encodings corresponding to the possible values in a Long-descriptor format translation table entry for stage 1 translations at ELn. See Memory types")
			if CRm == 13:
				if CRn == 0:
					if op2 == 2:
						return("TPIDR_EL3", "Read/Write Thread ID Register	Provides a location where software executing at ELn can store thread identifying information, for OS management purposes. See Context switching")
			if CRm == 12:
				if CRn == 0:
					if op2 == 1:
						return("RVBAR_EL3", "")
					if op2 == 0:
						return("VBAR_EL3", "Based Address Register	Holds the exception base address for any exception that is taken to ELn. See AArch64 exception table")
					if op2 == 2:
						return("RMR_EL3", "")
				if CRn == 12:
					if op2 == 5:
						return("ICC_SRE_EL3", "")
					if op2 == 4:
						return("ICC_CTLR_EL3", "")
					if op2 == 7:
						return("ICC_IGRPEN1_EL3", "")
			if CRm == 1:
				if CRn == 1:
					if op2 == 1:
						return("SDER32_EL3", "")
					if op2 == 0:
						return("SCR_EL3", "Configuration Register	Controls Secure state and trapping of exceptions to EL3. See Handling synchronous exceptions")
					if op2 == 2:
						return("CPTR_EL3", "")
				if CRn == 0:
					if op2 == 1:
						return("ACTLR_EL3[63:0]", "Control Register	Controls processor-specific features")
					if op2 == 0:
						return("SCTLR_EL3", "Control Register	Controls architectural features, for example the MMU, caches and alignment checking")
				if CRn == 3:
					if op2 == 1:
						return("MDCR_EL3", "")
				if CRn == 2:
					if op2 == 0:
						return("ZCR_EL3", "")
			if CRm == 2:
				if CRn == 0:
					if op2 == 0:
						return("TTBR0_EL3", "Table Base Register 1	Holds the base address of translation table 1, and information about the memory it occupies. This is one of the translation tables for the stage 1 translation of memory accesses at EL0 and EL1. See Separation of kernel and application Virtual Address spaces")
					if op2 == 2:
						return("TCR_EL3", "Control Register	Determines which of the Translation Table Base Registers define the base address for a translation table walk required for the stage 1 translation of a memory access from ELn. Also controls the translation table format and holds cacheability and shareability information. See Separation of kernel and application Virtual Address spaces")
			if CRm == 5:
				if CRn == 1:
					if op2 == 1:
						return("AFSR1_EL3", "")
					if op2 == 0:
						return("AFSR0_EL3", "")
				if CRn == 0:
					if op2 == 0:
						return("FAR_EL3", "Address Register	Holds the virtual faulting address. See Handling synchronous exceptions")
				if CRn == 2:
					if op2 == 0:
						return("ESR_EL3", "Syndrome Register	Includes information about the reasons for the exception. See The Exception Syndrome Register")
			if CRm == 4:
				if CRn == 1:
					if op2 == 0:
						return("SP_EL2", "")
				if CRn == 0:
					if op2 == 1:
						return("ELR_EL3", "Link Register	Holds the address of the instruction which caused the exception")
					if op2 == 0:
						return("SPSR_EL3", "Program Status Register	Holds the saved processor state when an exception is taken to this mode or Exception level")


if __name__ == "__main__":
	print(translate_sysinst(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
