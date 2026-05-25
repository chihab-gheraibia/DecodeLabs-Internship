# Dataset — UNSW-NB15

This project uses the **UNSW-NB15** dataset created by the Cyber Range Lab at the University of New South Wales (UNSW), Australia.

## How to Download

1. Visit the official dataset page:  
   👉 https://research.unsw.edu.au/projects/unsw-nb15-dataset

2. Download the following files:
   - `UNSW-NB15_1.csv`
   - `UNSW-NB15_2.csv`
   - `UNSW-NB15_3.csv`
   - `UNSW-NB15_4.csv`
   - `NUSW-NB15_features.csv` (feature names/descriptions)

3. Place all files in this `data/` folder.

## Dataset Details

| Property       | Value                                      |
|----------------|--------------------------------------------|
| Total Records  | ~2,540,000 network connection events       |
| Features       | 49 raw network traffic attributes          |
| Attack Types   | 9 categories + Normal traffic              |
| Format         | CSV (comma-separated)                      |
| Size (approx.) | ~1.2 GB total across all 4 files           |

## Attack Categories

| Category       | Description                                   |
|----------------|-----------------------------------------------|
| Normal         | Legitimate network traffic                    |
| DoS            | Denial of Service attacks                     |
| Exploits       | Software vulnerability exploitation           |
| Reconnaissance | Network scanning and information gathering    |
| Fuzzers        | Random/malformed packet injection             |
| Generic        | Generic attack patterns                       |
| Backdoors      | Remote access trojans                         |
| Shellcode      | Code injection attacks                        |
| Worms          | Self-propagating malware                      |
| Analysis       | Packet/file analysis attacks                  |

## Citation

> Moustafa, N., & Slay, J. (2015). UNSW-NB15: A comprehensive data set for network intrusion detection systems (UNSW-NB15 network data set). *2015 Military Communications and Information Systems Conference (MilCIS)*.

> Moustafa, N., & Slay, J. (2016). The evaluation of Network Anomaly Detection Systems: Statistical analysis of the UNSW-NB15 dataset and the comparison with the KDD99 dataset. *Information Security Journal: A Global Perspective*.
