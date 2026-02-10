# ASSIGNMENT
# Earth Meteorite Landings Analysis

## Task 1:
Extract programmatically the list of Earth Meteorite Landings from this dataset: [https://dmachek.github.io/meteorites-homework/meteorite_landings.json](https://dmachek.github.io/meteorites-homework/meteorite_landings.json)  
- How many entries are in the dataset?  
- What is the name and mass of the most massive meteorite in this dataset?  
- What is the most frequent year in this dataset?  

⚠️ **Provide your solution as a Pull Request to this repository.** ⚠️

**NOTE:** Please elaborate how did you get the results, provide the code or any means which you used to get to the results (regardless of the format/tools/framework which were used). Result itself is not sufficient.

---

# SOLUTION
# ☄️ Earth Meteorite Landings Analysis

![CI Status](https://github.com/barta-m/meteorites-hw/actions/workflows/pipeline.yml/badge.svg)

A programmatic analysis of the Earth Meteorite Landings dataset, featuring automated data fetching, cleaning, and statistical extraction.

## 🚀 Key Features
- **Automated Data Pipeline:** Fetches live data from the source, cleanses it, and calculates statistics.
- **Reproducible Environment:** Fully containerized using **Docker** for consistent execution.
- **CI/CD Integration:** GitHub Actions workflow automatically runs tests and executes the analysis on every push (or manually).

---

## 🛠️ How to Run

### Option A: GH Actions Pipeline
Runs automatically via GitHub Actions pipeline and shows results

### Option B: Using Docker
Run the analysis in an isolated container without installing Python locally.

1. **Build the image:**
   ```bash
   docker build -t meteorite-analysis .

2. **Run the analysis:**
   ```bash
   docker run --rm meteorite-analysis

3. **(Optional) Run tests inside Docker:**
   ```bash
   docker run --rm meteorite-analysis python -m pytest

### Option C: Local Python Environment
Prerequisites: Python 3.13+

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/barta-m/meteorites-hw.git](https://github.com/barta-m/meteorites-hw.git)
   cd meteorites-hw

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt

3. **Run the script:**
   ```bash
   python3 script.py