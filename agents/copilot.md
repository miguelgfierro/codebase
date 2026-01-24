# GitHub Copilot

GitHub Copilot is GitHub's AI-powered coding assistant.

## Installation

### Prerequisites

**Subscription:** Ensure you have one of the following:
- GitHub Copilot Individual subscription
- GitHub Copilot Business (via organization)
- GitHub Copilot Enterprise (via organization)
- GitHub Copilot Free (limited features)

### VSCode Extension

1. **Install Extension:**
   - Open VSCode
   - Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
   - Search for "GitHub Copilot"
   - Click **Install**

   Alternatively, install from the terminal:
   ```bash
   code --install-extension GitHub.copilot
   ```

2. **Install Copilot Chat (Recommended):**
   - Search for "GitHub Copilot Chat" in Extensions
   - Click **Install**

   Or via terminal:
   ```bash
   code --install-extension GitHub.copilot-chat
   ```

3. **Sign In:**
   - Click the Copilot icon in the status bar
   - Follow the GitHub authentication flow
   - Authorize the extension

### Agent Mode

To enable Copilot's agent mode for multi-step tasks:
1. Open VSCode Settings (Ctrl+, / Cmd+,)
2. Search for "Copilot Agent"
3. Enable agent mode features

## Usage

- **Inline Completions:** Start typing and Copilot suggests code
- **Chat:** Open Copilot Chat panel (Ctrl+Shift+I / Cmd+Shift+I)
- **Inline Chat:** Select code and press Ctrl+I / Cmd+I
- **Agent Mode:** Use `@workspace` in chat for multi-file tasks
