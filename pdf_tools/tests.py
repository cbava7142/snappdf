import os

CLERK_SECRET_KEY = os.environ["CLERK_SECRET_KEY"]
CLERK_AUTHORIZED_PARTIES = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

<script
  defer
  crossorigin="anonymous"
  src="https://YOUR_CLERK_FRONTEND_API/npm/@clerk/ui@1/dist/ui.browser.js"
></script>

<script
  defer
  crossorigin="anonymous"
  data-clerk-publishable-key="pk_test_REPLACE_ME"
  src="https://YOUR_CLERK_FRONTEND_API/npm/@clerk/clerk-js@6/dist/clerk.browser.js"
></script>

<script>
  window.addEventListener("load", async () => {
    await Clerk.load({
      ui: { ClerkUI: window.__internal_ClerkUICtor }
    });

    const authControls = document.getElementById("auth-controls");
    const signInButton = document.getElementById("sign-in-button");
    const signUpButton = document.getElementById("sign-up-button");
    const authPanel = document.getElementById("auth-panel");
    const signInMount = document.getElementById("sign-in-mount");
    const signUpMount = document.getElementById("sign-up-mount");

    function renderAuth() {
      if (Clerk.isSignedIn) {
        signInButton.hidden = true;
        signUpButton.hidden = true;
        Clerk.mountUserButton(document.getElementById("user-button"));
      } else {
        signInButton.hidden = false;
        signUpButton.hidden = false;
      }
    }

    signInButton.addEventListener("click", () => {
      authPanel.hidden = false;
      signUpMount.replaceChildren();
      Clerk.mountSignIn(signInMount);
    });

    signUpButton.addEventListener("click", () => {
      authPanel.hidden = false;
      signInMount.replaceChildren();
      Clerk.mountSignUp(signUpMount);
    });

    Clerk.addListener(renderAuth);
    renderAuth();
  });
</script>

<div id="auth-controls" class="flex items-center gap-2">
  <button id="sign-in-button" type="button">Sign in</button>
  <button id="sign-up-button" type="button">Sign up</button>
  <div id="user-button"></div>
</div>

<div id="auth-panel" hidden>
  <div id="sign-in-mount"></div>
  <div id="sign-up-mount"></div>
</div>

async function authenticatedFetch(url, options = {}) {
  if (!Clerk.session) {
    throw new Error("Please sign in first.");
  }

  const token = await Clerk.session.getToken();

  return fetch(url, {
    ...options,
    headers: {
      ...(options.headers || {}),
      Authorization: `Bearer ${token}`
    }
  });
}

from django.test import TestCase + current.endpoint, {
  method: "POST",
# Create your tests here.
});
