#!/usr/bin/env python3
import json

# Read the Lighthouse report
with open('lighthouse-report.json', 'r') as f:
    data = json.load(f)

# Extract main category scores
categories = data['categories']
print("=== LIGHTHOUSE ANALYSIS RESULTS ===")
print(f"Performance Score: {categories['performance']['score']}")
print(f"Accessibility Score: {categories['accessibility']['score']}")
print(f"Best Practices Score: {categories['best-practices']['score']}")
print(f"SEO Score: {categories['seo']['score']}")

print("\n=== KEY METRICS ===")
# Extract key performance metrics
audits = data['audits']
key_metrics = [
    'first-contentful-paint',
    'largest-contentful-paint', 
    'total-blocking-time',
    'cumulative-layout-shift',
    'speed-index'
]

for metric in key_metrics:
    if metric in audits:
        audit = audits[metric]
        print(f"{audit['title']}: {audit.get('numericValue', 'N/A')} (Score: {audit.get('score', 'N/A')})")

print("\n=== FAILING AUDITS ===")
# Find failing audits (score < 0.9)
failing_audits = []
for audit_id, audit_data in audits.items():
    if audit_data.get('score') is not None and audit_data['score'] < 0.9:
        failing_audits.append({
            'id': audit_id,
            'title': audit_data['title'],
            'score': audit_data['score'],
            'description': audit_data.get('description', '')
        })

# Sort by score (worst first)
failing_audits.sort(key=lambda x: x['score'])

for audit in failing_audits[:10]:  # Show top 10 failing audits
    print(f"❌ {audit['title']} (Score: {audit['score']})")
    print(f"   {audit['description'][:100]}...")
    print()
