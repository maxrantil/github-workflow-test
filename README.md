# GitHub Workflow Test Repository

This repository is used to test reusable workflows from `maxrantil/.github`.

## Phase 2: Issue Workflows

Testing 4 issue validation workflows:

1. **issue-ai-attribution-check** - Blocks AI/agent attribution
2. **issue-format-check** - Validates issue completeness
3. **issue-prd-reminder** - Reminds about PRD/PDR for features
4. **issue-auto-label** - Auto-labels issues

## Test Plan

### Test Cases to Create:

1. **AI Attribution Test** (should FAIL):
   - Title: "Add new feature"
   - Body: "Need to add X. Generated with Claude Code"

2. **Empty Issue Test** (should FAIL):
   - Title: "Fix bug"
   - Body: ""

3. **Valid Feature Request** (should PASS + get PRD reminder):
   - Title: "Add dark mode support"
   - Body: "Users want dark mode. Should toggle in settings."
   - Labels: enhancement

4. **Valid Bug Report** (should PASS + auto-label as bug):
   - Title: "App crashes on startup"
   - Body: "App crashes when launched. Steps: 1. Open app 2. See crash. Expected: app opens. Actual: crash."

5. **Multiple Label Test** (should auto-label with multiple labels):
   - Title: "Security vulnerability in authentication"
   - Body: "Found XSS vulnerability in login form. Need to fix urgently."

## Phase 3: Commit Quality Check

Testing commit quality workflow with fixup commits.

## Expected Results:

- Tests 1 & 2: Workflow FAILS, comment posted, label added
- Test 3: Workflow PASSES, PRD reminder posted, auto-labeled
- Test 4: Workflow PASSES, auto-labeled as 'bug'
- Test 5: Auto-labeled as 'security', 'bug', 'priority: high'
