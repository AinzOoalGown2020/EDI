! Fichier ENT1 : 
!===========================================================
! Ligne : ENT1 
!===========================================================
! CHAMP : TAB 
#define S_ENT1_TAB peel(pick(nPos, 1, 4), " ")
#define R_ENT1_TAB(A) put(nRec, 1, A :4.4)
!-----------------------------------------------------------
! CHAMP : numMSG 
#define S_ENT1_numMSG peel(pick(nPos, 5, 15), " ")
#define R_ENT1_numMSG(A) put(nRec, 5, A :15.15)
!-----------------------------------------------------------
! CHAMP : dateMSG 
#define S_ENT1_dateMSG peel(pick(nPos, 20, 8), " ")
#define R_ENT1_dateMSG(A) put(nRec, 20, A :8.8)
!-----------------------------------------------------------
!===========================================================
! Ligne : ENT2 
!===========================================================
! CHAMP : TAB 
#define S_ENT2_TAB peel(pick(nPos, 1, 4), " ")
#define R_ENT2_TAB(A) put(nRec, 1, A :4.4)
!-----------------------------------------------------------
! CHAMP : GLN 
#define S_ENT2_GLN peel(pick(nPos, 5, 13), " ")
#define R_ENT2_GLN(A) put(nRec, 5, A :13.13)
!-----------------------------------------------------------
! CHAMP : txtADDRESS 
#define S_ENT2_txtADDRESS peel(pick(nPos, 18, 70), " ")
#define R_ENT2_txtADDRESS(A) put(nRec, 18, A :70.70)
!-----------------------------------------------------------
! CHAMP : numCODEP 
#define S_ENT2_numCODEP peel(pick(nPos, 88, 5), " ")
#define R_ENT2_numCODEP(A) put(nRec, 88, A :5.5)
!-----------------------------------------------------------
! CHAMP : txtVILLE 
#define S_ENT2_txtVILLE peel(pick(nPos, 93, 50), " ")
#define R_ENT2_txtVILLE(A) put(nRec, 93, A :50.50)
!-----------------------------------------------------------
!===========================================================
! Ligne : ART1 
!===========================================================
! CHAMP : TAB 
#define S_ART1_TAB peel(pick(nPos, 1, 4), " ")
#define R_ART1_TAB(A) put(nRec, 1, A :4.4)
!-----------------------------------------------------------
! CHAMP : GTIN 
#define S_ART1_GTIN peel(pick(nPos, 5, 13), " ")
#define R_ART1_GTIN(A) put(nRec, 5, A :13.13)
!-----------------------------------------------------------
! CHAMP : LABEL 
#define S_ART1_LABEL peel(pick(nPos, 18, 52), " ")
#define R_ART1_LABEL(A) put(nRec, 18, A :52.52)
!-----------------------------------------------------------
! CHAMP : COMMENT 
#define S_ART1_COMMENT peel(pick(nPos, 70, 50), " ")
#define R_ART1_COMMENT(A) put(nRec, 70, A :50.50)
!-----------------------------------------------------------
