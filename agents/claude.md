# Claude Code

Claude Code is Anthropic's official agentic coding tool that lives in your terminal and IDE.

## Installation

### Standalone (Terminal)

**Prerequisites:**
- Node.js 18+

**Option 1: npm (Recommended)**
```bash
npm install -g @anthropic-ai/claude-code
```

**Option 2: Homebrew (macOS/Linux)**
```bash
brew install claude-code
```

**First Run:**
```bash
claude
```

On first launch, you'll be prompted to authenticate with your Anthropic account.

### VSCode Extension

1. Open VSCode
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "Claude Code"
4. Click **Install** on the official Anthropic extension
5. After installation, open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
6. Run `Claude Code: Open`

Alternatively, install from the terminal:
```bash
code --install-extension anthropic.claude-code
```

## Authentication

Claude Code requires an Anthropic account. On first use:
1. Run `claude` in terminal or open Claude Code in VSCode
2. Follow the browser authentication flow
3. Your session will be saved for future use

## Usage

- **Terminal:** Run `claude` to start an interactive session
- **VSCode:** Use the Claude Code panel or Command Palette commands
- **Help:** Run `claude --help` or type `/help` in a session
