# Critique of app1.py

## Loyalty Dashboard
- Displays a static loyalty card with hardcoded points, a progress bar, and a "View Rewards" button using HTML/CSS.
- I would connect the points and progress to a backend service, make the card interactive, and ensure accessibility.
- Hardcoded point values and lack of real user authentication make this unfit for production.

## Station Finder
- Lets users input a city and returns a hardcoded station address if found, otherwise shows an error.
- I would integrate a real-time station database or API, add location auto-complete, and handle errors gracefully.
- Hardcoded station data and no input validation or error logging are unacceptable for a real deployment.

## Fuel Calculator
- Calculates fuel cost based on user input and hardcoded prices, displaying the result in the UI.
- I would fetch live fuel prices from an external service, add input validation, and provide a receipt or transaction log.
- Using hardcoded prices and not validating user input is not suitable for a production environment.

## Navigation Bar
- Renders a fixed bottom navigation bar with static SVG icons and labels for navigation, but no real routing logic.
- I would implement true page routing, use accessible SVGs or icon libraries, and highlight the active page.
- Static navigation with no state or routing logic is not shippable for a scalable, maintainable app.