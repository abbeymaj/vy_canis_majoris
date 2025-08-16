## VY Canis Majoris - Data Loading Pipeline

The objective of this project is to fetch and store the Magnitude data for VY Canis Majoris from the Association of Variable Star Observers (AAVSO) website. 

The project defines an Extract Transform Load (ETL) pipeline that cleans, transforms and then loads the fetched data into a SQLite database.

The database is updated on a weekly basis (every Sunday) by a cron job that leverages GitHub Actions to trigger the job.
The project exposes the link to the database via an API, which was created using GitHub Pages. This enables the data to be used by other programs or for analysis.

The project has been created using Python and its associated libraries. 

### About VY Canis Majoris

VY Canis Majoris is a remarkable red hypergiant star located in the constellation Canis Major, approximately 3,800 light-years from Earth. Known for its extreme size and variability, it is one of the largest known stars in the Milky Way, with a radius estimated to be over 1,000 times that of the Sun. VY Canis Majoris is a semi-regular variable star, exhibiting unpredictable changes in brightness due to complex pulsations and massive ejections of stellar material. Surrounded by a dense nebula formed from its own expelled gas and dust, this stellar titan offers a rare glimpse into the final evolutionary stages of massive stars before they explode as supernovae.

![VY Canis Majoris](https://github.com/abbeymaj80/my-ml-datasets/blob/master/screenshots/canis_majoris/vy_canis_majoris.jpg)

 Here are some fascinating facts that highlight its cosmic extremes:

- 🌌 **Enormous Size**: Estimated to be **1,420 times the radius of the Sun**. If placed at the center of our solar system, its surface would reach beyond Jupiter's orbit.
- 🔥 **Extreme Luminosity**: Shines with a brightness **~270,000 times greater than the Sun**, making it one of the most luminous stars in the Milky Way.
- 🌪️ **Massive Mass Loss**: Sheds **~30 Earth masses per year**, forming a vast, asymmetric nebula of gas and dust around it.
- 🌀 **Variable Star**: Classified as a **semi-regular variable**, with unpredictable brightness changes due to pulsations and chaotic mass ejections.
- 💥 **Hypernova Potential**: Expected to end its life in a **hypernova**, an explosion up to **100× more energetic** than a typical supernova.
- 🧊 **Cool Surface**: Despite its brilliance, its surface temperature is relatively low at **~3,490 K**, cooler than the Sun.
- 🧪 **Chemical Richness**: Emits strong **maser signals** and hosts a variety of molecules in its surrounding envelope, typical of OH/IR stars.

> 🧭 VY Canis Majoris offers a rare glimpse into the final, turbulent stages of stellar evolution for massive stars.


### Project Installation

Install the project using pip. It is always recommended to use a virtual environment (for example, using anaconda) to do the installation.

This project was built using Python 3.9.

To install the project, use the following: 

```bash
  pip install -r requirements.txt
```
    
### Tech Stack

**Language:** Python

**CI/CD:** GitHub Actions

**Database:** SQLite

**API:** GitHub Pages

## High-Level Design Documentation

The high-level design diagram for the ETL pipeline of the project is depicted below:

![High-Level Design Diagram](https://github.com/abbeymaj80/my-ml-datasets/blob/master/screenshots/canis_majoris/High_Level_Design.png)

Detailed information on the project as well as the ETL process can be found in the project's high-level design document.

The link to the high-level design document is as follows:

![VY Canis Majoris Magnitude Data Load - High-Level Design Document](https://github.com/abbeymaj80/my-ml-datasets/raw/refs/heads/master/Design_Docs/VYCMA_Load_Data_HLD.docx)

### References

- ![American Association of Variable Star Observers Website](https://www.aavso.org/)
- ![VY Canis Majoris Wikipedia Page](https://en.wikipedia.org/wiki/VY_Canis_Majoris)