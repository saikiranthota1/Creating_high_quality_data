# Asana Data Simulation

This project simulates Asana data including users, projects, and tasks.

## Setup

    ```
    pip install -r requirements.txt
    ```

2. **Set up environment variables**:
   Copy `.env.example` to `.env`. This project uses `python-dotenv` to manage configuration.
   ```bash
   cp .env.example .env
   ```
   **Configuration Options**:
   - `DB_PATH`: Location of the SQLite database.
   - `ORG_NAME`: Name of the simulated organization.
   - `EMPLOYEE_COUNT`: Number of users to generate (e.g., 50).
   - `HISTORY_MONTHS`: Duration of history to simulate (e.g., 6).

3. **Run the simulation**:
   ```bash
   python src/main.py
   ```
   Logs will be available in `output/simulation.log`.

4. **Inspect Results**:
   Run the inspection script to view database statistics:
   ```bash
   python src/inspect_db.py
   ```

## Architecture
- **src/generators/**: Modular data generation logic independent of the database adaptation.
- **src/utils/**: Helper functions for dates, logging, and IDs.
- **src/models/**: Data models and enumerations.
- **schema.sql**: Database schema definition.
