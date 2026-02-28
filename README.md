# Investing Screener

   Quantitative stock screener for momentum-based trading strategies.

   ## Features

   - [ ] Data pipeline with yfinance
   - [ ] Momentum strategy implementation
   - [ ] Backtesting framework
   - [ ] Performance analytics

   ## Project Structure

 ```

 investing-screener/
 ├── src/           # Source code
 ├── tests/         # Unit tests
 ├── data/          # Data storage
 ├── docs/          # Documentation
 └── notebooks/     # Jupyter notebooks

 ```

   ## Setup

   ```bash
   # Clone repository
   git clone https://github.com/forgion/investing-screener.git
   cd investing-screener

   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate   # Windows

   # Install dependencies
   pip install -r requirements.txt
 ```

 Usage

 ```python
   from src.screener import MomentumScreener

   screener = MomentumScreener()
   results = screener.run()
 ```

 Roadmap

 - Phase 1: Data pipeline & basic screener
 - Phase 2: Strategy validation & backtesting
 - Phase 3: Live testing with small positions
 - Phase 4: Scaling & automation

 License

 MIT License - see LICENSE file.