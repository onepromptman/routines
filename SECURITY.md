# Security

## What this repository holds

Recipes (Markdown) and a downloadable kit. The kit's plugins run inside the Claude desktop app on your computer. They read public websites, write files only into the folder you choose, and send nothing anywhere else.

## Report a problem

If you find a security problem, open a private report through this repository's **Security** tab (Report a vulnerability). If that tab is not available to you, open an issue that says only that you have a security report, without details, and we will reply with a private channel.

Please do not post exploit details in a public issue.

## What counts

- A plugin reading or writing outside the folder you chose.
- A plugin sending data anywhere other than the public sites it reads and Claude itself.
- A secret, an API key or personal data committed to this repository or shipped in the kit.
- A way to make a scheduled run take an action the recipe says it never takes (send, post, publish, push).

## What does not count

- Behavior of the Claude desktop app itself. Report that to Anthropic.
- A public website refusing or rate-limiting a request.
