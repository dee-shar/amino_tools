# Amino Tools 🚀

Advanced automation toolkit for Amino apps with enhanced security and performance.

## Features ✨
- Multi-account support
- Rate-limited API calls
- Proxy integration
- Comprehensive logging
- Modular design for easy customization

## Installation (Termux) 📲

```bash
# 1. Update packages
pkg update -y && pkg upgrade -y

# 2. Install dependencies
pkg install -y python git openssl

# 3. Clone repository
git clone https://github.com/dee-shar/amino_tools
cd amino_tools

# 4. Setup virtual environment
python -m venv venv
source venv/bin/activate

# 5. Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# 6. Run with safety checks
python -O main.py --safe-mode

# Run with proxy support
python main.py --proxy socks5://user:pass@host:port

# Use config file
python main.py --config settings.ini

# Enable debug logging
python main.py --log-level DEBUG
```
