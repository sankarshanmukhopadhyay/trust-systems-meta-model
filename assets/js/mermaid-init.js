import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";
mermaid.initialize({ startOnLoad: false, securityLevel: "strict", theme: "neutral" });
const nodes = document.querySelectorAll("pre > code.language-mermaid");
nodes.forEach((code, index) => {
  const container = document.createElement("div");
  container.className = "mermaid";
  container.id = `mermaid-${index}`;
  container.textContent = code.textContent;
  code.parentElement.replaceWith(container);
});
if (nodes.length) await mermaid.run({ querySelector: ".mermaid" });
