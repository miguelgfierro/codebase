# Gemini Code Assist

Gemini Code Assist is Google's AI-powered coding assistant for VS Code.

## Installation - "Most Features" Version

### Prerequisites

**Subscription:** Ensure you have one of the following:
- Gemini for Google Cloud license (Enterprise is best for private repos)
- Google AI Pro subscription

### Setup Steps

1. **Install Extension:**
   Download the Gemini Code Assist extension from the VS Code Marketplace.
   - Open VSCode
   - Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
   - Search for "Gemini Code Assist"
   - Click **Install**

2. **Enable Agent Mode:**
   - Open VSCode Settings (Ctrl+, / Cmd+,)
   - Search for "Gemini Agent Mode"
   - Toggle **"Enable Agent Mode (Preview/GA)"** to enabled

3. **Install Gemini CLI:**
   In your integrated terminal, run:
   ```bash
   npm install -g @google/gemini-cli
   ```

   Then link it to your VS Code:
   ```bash
   /ide install
   ```

## Usage

Once configured, Gemini Code Assist provides:
- Code completions and suggestions
- Agent mode for multi-step coding tasks
- Integration with Google Cloud services
