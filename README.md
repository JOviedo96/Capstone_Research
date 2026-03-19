# Capstone_Research

## Health App Competitor Review Analysis
A pipeline for scraping, cleaning, and analyzing user reviews from competing health and consumer apps — used to surface feature gaps, user pain points, and design patterns to inform a health advocacy app.

## Overview
This project collects thousands of App Store and Google Play reviews across a curated set of direct healthcare competitors and indirect consumer app comparisons. Reviews are then cleaned, filtered for feature relevance, and analyzed to extract sentiment scores, user personas, feature priorities, and journey maps.
The analysis is intended to support product and UX strategy decisions for a health advocacy application — specifically around provider communication, insurance navigation, health data tracking, and patient self-advocacy tools.

## Repository Structure
├── scraper.py                  # Scrapes App Store and Google Play reviews
├── sentiment_analysis.ipynb    # Full analysis pipeline (10-step notebook)
└── competitor_reviews.csv      # Raw scraped reviews (not committed — see note below)

Note: competitor_reviews.csv is excluded from this repository due to file size. Run scraper.py to regenerate it locally.


## Competitors Analyzed
Direct Healthcare Competitors
AppPlatformWebMDiOS + AndroidMyChart (Epic)iOS + AndroidAda HealthiOS + AndroidMayo CliniciOS + AndroidGoodRXiOS + AndroidZocDociOS + AndroidApple HealthiOS only
Indirect Competitors (Design Pattern Reference)
AppWhy IncludedRedfinSearch & discovery UXCredit KarmaMaking complex information accessibleLose ItHealth tracking UX patterns

## Setup
Prerequisites

Python 3.8+
pip

## Installation
cd health-app-competitor-analysis
pip install -r requirements.txt
Required packages
pandas
numpy
matplotlib
seaborn
textblob
app-store-web-scraper
google-play-scraper

## Usage
Step 1 — Scrape Reviews
bashpython scraper.py
This will scrape App Store and Google Play reviews for all configured competitors and save the results to competitor_reviews.csv. The CSV contains the following columns:
ColumnDescriptionidReview IDratingStar rating (1–5)titleReview titlecontentReview body textdateReview datesourceapple or googlecompetitorApp name
Step 2 — Run the Analysis Notebook
Open sentiment_analysis.ipynb in Jupyter and run the cells in order. Each step is self-contained:
StepDescription1Data loading and initial exploration2Data quality assessment and distribution3Basic cleaning (deduplication, null removal, English filtering)4Feature-focused filtering (removes technical complaints, keeps UX/feature discussions)5Feature category extraction and sentiment scoring per competitor6User needs and pain point extraction7Feature gap analysis and strategic recommendations8Competitive feature matrix with heatmap visualizations9Data-driven user persona development10User journey mapping and feature prioritization

## Key Outputs
Feature Gap Analysis — Scores each product area by market gap and average user sentiment to identify the highest-opportunity features.
Competitive Heatmaps — Visual matrices comparing feature strength, user sentiment, and market coverage across all competitors.
User Personas — Five data-derived personas built from review patterns, including goals, frustrations, and preferred features.
Feature Priority Ranking — A scored roadmap ranking 8 candidate features by user impact, market gap, technical feasibility, and development effort.
User Journey Maps — Three core journeys (new diagnosis, appointment advocacy, insurance navigation) mapped with emotional states, pain points, and product opportunities at each stage.

## Key Findings

Provider communication has the lowest sentiment (0.16) across all healthcare apps — the largest single opportunity area.
Apple Health consistently scores lowest across every feature category despite high usage, signaling an unfilled market need.
GoodRX leads in UX sentiment (0.45) and insurance navigation — the strongest design reference for complex health data.
Credit Karma and Lose It demonstrate that indirect apps set the benchmark for accessible, trackable user experiences.


## Limitations

App Store reviews are capped by the scraper library; very old reviews may not be captured.
Google Play reviews are sorted by newest — historical coverage varies by app.
Sentiment scoring uses TextBlob, which is a general-purpose model and may not capture healthcare-specific nuance.
English-language filter uses an ASCII heuristic and may occasionally exclude valid reviews.
