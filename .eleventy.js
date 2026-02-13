module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/styles.css");
  eleventyConfig.addPassthroughCopy("src/admin");
  eleventyConfig.addPassthroughCopy("src/images");

  // Markdown filter for rendering CMS markdown fields in templates
  const markdownIt = require("markdown-it");
  const md = markdownIt({ html: true, breaks: true, linkify: true });
  eleventyConfig.addFilter("md", value => value ? md.render(value) : "");

  eleventyConfig.addCollection("experiences", c =>
    c.getFilteredByGlob("src/experiences/*.md").sort((a, b) => (a.data.order || 0) - (b.data.order || 0))
  );
  eleventyConfig.addCollection("projects", c =>
    c.getFilteredByGlob("src/projects/*.md").sort((a, b) => (a.data.order || 0) - (b.data.order || 0))
  );
  eleventyConfig.addCollection("countries", c =>
    c.getFilteredByGlob("src/countries/*.md").sort((a, b) => (a.data.order || 0) - (b.data.order || 0))
  );
  eleventyConfig.addCollection("posts", c =>
    c.getFilteredByGlob("src/blog/*.md").sort((a, b) => b.date - a.date)
  );

  eleventyConfig.addFilter("limit", (arr, count) => (arr || []).slice(0, count));
  eleventyConfig.addFilter("head", (arr, count) => (arr || []).slice(0, count));

  return {
    dir: { input: "src", includes: "_includes", data: "_data", output: "_site" },
    templateFormats: ["njk", "md", "html"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk"
  };
};
