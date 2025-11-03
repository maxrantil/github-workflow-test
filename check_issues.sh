#!/bin/bash
for i in {74..86}; do
  echo "=== Issue #$i ==="
  gh issue view $i --json title,labels --jq '.title + " | Labels: " + ([.labels[].name] | join(", "))'
  echo -n "PRD Reminder: "
  gh issue view $i --comments | grep -q "Feature Request Workflow Reminder" && echo "✅ POSTED" || echo "❌ NOT POSTED"
  echo
done
