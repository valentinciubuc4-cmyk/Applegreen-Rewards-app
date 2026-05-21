# Applegreen Go – Developer Ledger

## Lesson 3
- Initial Streamlit prototype with static mockups and basic navigation.

## Lesson 4
- Added SQLite integration and dynamic dashboard metrics.
- Implemented session state for user login and navigation.

## Lesson 5
- Migrated to live Google Maps iframe for station finder.
- Introduced branded dashboard visuals and rewards logic.
- Added session-driven login gate and sidebar logout.

## Lesson 6
- [Troubleshooting, Compliance]  
  Removed all obsolete layout properties and unexpected keyword arguments from the codebase.  
  Ensured `st.iframe` uses only supported parameters, and all images/dataframes use the new `width='stretch'` protocol for 2026 compliance.  
  Eradicated the unexpected keyword parameter crash in the Station Finder map, restoring full application execution and navigation.
- [State-Management, UI/UX, Hotfixes]  
  Restored native Streamlit button navigation for the bottom navbar to preserve session state and prevent forced logouts.  
  Applied strict CSS flexbox overrides to lock navigation into a single horizontal row, eliminating vertical stacking on mobile and desktop.
- [UI/UX, Emoji, Accessibility]  
  Replaced all SVG/HTML button labels with clean emoji text labels to guarantee perfect rendering and accessibility on all platforms.

# Lesson 3: Prototype & Environment

## Design Concept
### Prompt 1 [UI/UX]
- Describe the desired Applegreen UI with a clean white background, emerald green and lime green palette, and a gradient loyalty card.

**Result:** The AI generated XAML and Streamlit/CSS code samples using the specified colors, gradients, and layout for a modern, branded look.

## Technology Pivot
### Prompt 2 [State-Management]
- Move from a simple console-based Python script to a visual, interactive Streamlit "Page App" with multiple pages.

**Result:** The AI provided a Streamlit app template with Dashboard, Station Finder, and Fuel Calculator pages, using session state and custom navigation.

## Environment Fix
### Prompt 3 [Troubleshooting]
- Troubleshoot and resolve the "zsh: command not found: pip" error on my MacBook Pro to enable Python package installation.

**Result:** The AI gave Mac-specific terminal commands to install pip and ensure the Python environment was correctly set up.

## Refinement
### Prompt 4 [UI/UX]
- Request custom CSS injection to match the Applegreen design as shown in image.jpg, including button styles and font choices.

**Result:** The AI supplied CSS snippets for Streamlit to style buttons, fonts, and layout, achieving a closer visual match to the brand.

---

# Lesson 6: Mapping & Visual Upgrades

## Live Map Integration
### Prompt 5 [API-Integration, Embeds]
- Replace static station lookup with a live, embedded Google Maps iframe that dynamically queries for Applegreen locations based on user input.

**Result:** The Station Finder page now renders a real-time map for any Irish city or town, providing instant, interactive geographic context for users.

## Real Station Imagery
### Prompt 6 [UI/UX, Media-Management]
- Swap out placeholder text and static icons for real, web-hosted Applegreen forecourt images in dashboard and station views.

**Result:** The app now loads and displays authentic station photos, enhancing realism and user trust.

---

# Summary

This log demonstrates a progression from static UI concepts to a fully interactive, data-driven, and visually authentic prototype, with each iteration
