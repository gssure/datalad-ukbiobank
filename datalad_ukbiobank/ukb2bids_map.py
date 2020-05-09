# This file has been modified from its original form.
# Parts of the data was originally taken from: https://git.fmrib.ox.ac.uk/falmagro/UK_biobank_pipeline_v_1/blob/master/bb_data/UKBB_to_BIDS.json
# It was modified to default to relative pathing (without "BIDS/" top-level directory)

# within-participant folder filename mapping
# we make no distinction between a derivative or a raw component
# to allow users to assemble datasets into larger BIDS-compliant
# superdatasets that could either be raw data or derivatives
ukb2bids = {
# top-level
'20252_0/T1': '{unrecogdir}/T1',
'20253_0/T2_FLAIR': '{unrecogdir}/T2_FLAIR',
'20250_0/fieldmap': '{unrecogdir}/fieldmap',
'20250_0/dMRI': '{unrecogdir}/dMRI',
'20251_0/SWI': '{unrecogdir}/SWI',
'20227_0/fMRI': '{unrecogdir}/fMRI',
'20249_0/fMRI': '{unrecogdir}/fMRI',
'25747_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-hariri_eprime',
'25748_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-hariri_eprime',
'25749_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-hariri_eprime',
'25750_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-rest_full_correlation_matrix_d25',
'25751_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-rest_full_correlation_matrix_d100',
'25752_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-rest_partial_correlation_matrix_d25',
'25753_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-rest_partial_correlation_matrix_d100',
'25754_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-rest_component_amplitudes_d25',
'25755_0': '{unrecogdir}/fMRI/sub-{subj}_{session}_task-rest_component_amplitudes_d100',
# raw
'20252_0/T1/T1': '{session}/anat/sub-{subj}_{session}_T1w',
'20250_0/dMRI/raw/AP': '{session}/dwi/sub-{subj}_{session}_acq-AP_dwi',
'20250_0/dMRI/raw/PA': '{session}/dwi/sub-{subj}_{session}_acq-PA_dwi',
'20249_0/fMRI/tfMRI': '{session}/func/sub-{subj}_{session}_task-hariri_bold',
'20227_0/fMRI/rfMRI': '{session}/func/sub-{subj}_{session}_task-rest_bold',
'20249_0/fMRI/tfMRI_SBREF': '{session}/func/sub-{subj}_{session}_task-rest_sbref',
'20227_0/fMRI/rfMRI_SBREF': '{session}/func/sub-{subj}_{session}_task-hariri_sbref',
'20253_0/T2_FLAIR/T2_FLAIR': '{session}/anat/sub-{subj}_{session}_FLAIR',
'raw/T1_notNorm': '{session}/anat/sub-{subj}_{session}_acq-notNorm_T1w',
'raw/T2_FLAIR_notNorm': '{session}/anat/sub-{subj}_{session}_acq-notNorm_FLAIR',
'raw/AP_SBREF': '{session}/dwi/sub-{subj}_{session}_acq-AP_sbref',
'raw/PA_SBREF': '{session}/dwi/sub-{subj}_{session}_acq-PA_sbref',
# SWI
# As of this writing, SWI was an inactive BEP with last contributions from several months ago. We're putting them in the
# source folder since there's no specs for the format.
# https://docs.google.com/document/d/1kyw9mGgacNqeMbp4xZet3RnDhcMmf4_BmRgKaOkO2Sc/view#
'raw/SWI_TOTAL_MAG_notNorm_TE2': '{session}/swi/sub-{subj}_{session}_part-mag_echo-2_GRE',
'raw/SWI_TOTAL_MAG_notNorm': '{session}/swi/sub-{subj}_{session}_part-mag_echo-1_GRE',
'20251_0/SWI/SWI_TOTAL_MAG': '{session}/swi/sub-{subj}_{session}_part-mag_echo-1_rec-norm_GRE',
'20251_0/SWI/SWI_TOTAL_PHA': '{session}/swi/sub-{subj}_{session}_part-phase_echo-1_GRE',
'20251_0/SWI/SWI_TOTAL_MAG_TE2': '{session}/swi/sub-{subj}_{session}_part-mag_echo-2_rec-norm_GRE',
'20251_0/SWI/SWI_TOTAL_PHA_TE2': '{session}/swi/sub-{subj}_{session}_part-phase_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL26_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-26_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL21_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-21_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL15_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-15_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL09_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-09_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL08_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-08_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL22_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-22_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL28_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-28_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL29_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-29_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL08_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-08_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL05_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-05_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL12_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-12_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL12_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-12_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL30_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-30_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL05_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-05_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL09_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-09_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL01_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-01_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL13_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-13_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL13_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-13_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL21_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-21_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL22_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-22_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL10_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-10_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL12_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-12_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL15_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-15_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL09_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-09_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL16_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-16_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL18_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-18_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL23_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-23_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL30_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-30_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL31_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-31_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL02_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-02_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL07_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-07_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL31_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-31_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL29_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-29_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL13_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-13_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL24_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-24_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL19_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-19_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL25_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-25_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL25_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-25_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL24_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-24_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL22_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-22_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL01_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-01_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL04_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-04_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL27_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-27_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL27_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-27_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL14_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-14_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL01_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-01_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL28_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-28_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL03_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-03_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL30_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-30_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL15_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-15_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL23_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-23_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL28_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-28_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL27_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-27_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL19_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-19_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL16_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-16_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL05_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-05_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL32_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-32_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL07_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-07_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL02_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-02_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL01_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-01_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL30_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-30_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL23_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-23_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL26_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-26_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL09_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-09_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL03_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-03_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL17_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-17_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL12_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-12_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL06_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-06_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL11_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-11_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL31_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-31_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL11_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-11_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL21_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-21_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL22_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-22_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL06_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-06_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL11_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-11_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL25_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-25_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL16_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-16_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL31_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-31_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL07_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-07_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL04_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-04_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL27_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-27_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL24_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-24_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL17_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-17_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL19_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-19_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL20_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-20_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL18_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-18_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL24_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-24_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL19_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-19_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL20_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-20_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL29_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-29_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL32_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-32_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL29_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-29_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL02_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-02_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL20_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-20_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL28_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-28_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL26_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-26_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL07_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-07_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL04_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-04_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL25_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-25_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL18_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-18_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL18_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-18_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL21_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-21_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL32_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-32_echo-1_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL13_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-13_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL08_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-08_echo-1_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL20_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-20_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL14_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-14_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL23_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-23_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL17_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-17_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL15_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-15_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL08_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-08_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL06_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-06_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL03_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-03_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL17_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-17_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL02_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-02_echo-2_GRE',
'20251_0/SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL10_ECHO1_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-10_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL03_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-03_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL16_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-16_echo-2_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL04_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-04_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL14_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-14_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL26_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-26_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL14_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-14_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL10_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-10_echo-2_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL10_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-10_echo-1_GRE',
'20251_0/SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL32_ECHO1_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-32_echo-1_GRE',
'20251_0/SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL05_ECHO2_20': '{session}/swi/sub-{subj}_{session}_part-phase_coil-05_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL06_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-06_echo-2_GRE',
'20251_0/SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL11_ECHO2_17': '{session}/swi/sub-{subj}_{session}_part-mag_coil-11_echo-2_GRE',
}
