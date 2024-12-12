
# 📄 Markdown Syntax Cheat Sheet

---

## 1. Headings
Use `#` for headings. The number of `#` determines the heading level.

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

### Result:
# Heading 1  
## Heading 2  
### Heading 3  
#### Heading 4  
##### Heading 5  
###### Heading 6  

---

## 2. Text Formatting

```markdown
**Bold Text**
*Italic Text*
***Bold and Italic***
~~Strikethrough~~
```

### Result:
**Bold Text**  
*Italic Text*  
***Bold and Italic***  
~~Strikethrough~~  

---

## 3. Lists

### Unordered List:
Use `-`, `*`, or `+`.

```markdown
- Item 1
- Item 2
  - Sub-item 1
  - Sub-item 2
```

### Result:
- Item 1  
- Item 2  
  - Sub-item 1  
  - Sub-item 2  

### Ordered List:
Use numbers.

```markdown
1. First item
2. Second item
3. Third item
   1. Sub-item 1
   2. Sub-item 2
```

### Result:
1. First item  
2. Second item  
3. Third item  
   1. Sub-item 1  
   2. Sub-item 2  

---

## 4. Links and Images

### Links:
```markdown
[Text to display](https://example.com)
```

### Result:  
[Text to display](https://example.com)

### Images:
```markdown
![Alt Text](https://example.com/image.jpg)
```

### Result:  
![Alt Text](https://example.com/image.jpg)

---

## 5. Quotes

Use `>` for blockquotes.

```markdown
> This is a blockquote.
> It spans multiple lines.
```

### Result:
> This is a blockquote.  
> It spans multiple lines.

---

## 6. Code Blocks

### Inline Code:
Wrap code with backticks: `` `code` ``

```markdown
This is an `inline code` example.
```

### Result:  
This is an `inline code` example.

### Multi-line Code Block:
Wrap code with triple backticks.

\`\`\`language  
print("Hello, World!")  
\`\`\`

### Result:

```python
print("Hello, World!")
```

---

## 7. Horizontal Line

Use `---` or `***` for a horizontal line.

```markdown
---
```

### Result:  
---

---

## 8. Tables

```markdown
| Header 1   | Header 2   | Header 3   |
|------------|------------|------------|
| Row 1 Col1 | Row 1 Col2 | Row 1 Col3 |
| Row 2 Col1 | Row 2 Col2 | Row 2 Col3 |
```

### Result:
| Header 1   | Header 2   | Header 3   |
|------------|------------|------------|
| Row 1 Col1 | Row 1 Col2 | Row 1 Col3 |
| Row 2 Col1 | Row 2 Col2 | Row 2 Col3 |

---

## 9. Task Lists

Use `- [ ]` for task lists.

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

### Result:
- [x] Completed task  
- [ ] Incomplete task  
- [ ] Another task  

---

## 10. Footnotes

Add footnotes using `[^1]` and define them at the bottom.

```markdown
This is an example of a footnote.[^1]

[^1]: This is the footnote text.
```

### Result:  
This is an example of a footnote.[^1]  

[^1]: This is the footnote text.

---

## 11. Embedding Files and Links (Obsidian Specific)

```markdown
![[local-file.jpg]]
[[note-link]]
```

### Result:  
- `![[local-file.jpg]]` embeds a local image.  
- `[[note-link]]` links to another note in Obsidian.

---

## 12. Checkboxes (Obsidian Specific)

Interactive checklists are supported in Obsidian.

```markdown
- [ ] Task 1
- [x] Task 2 (completed)
- [ ] Task 3
```

---

## 13. Highlight Text (Obsidian Specific)

Use `==` to highlight text.

```markdown
This is ==highlighted text==.
```

### Result:
This is ==highlighted text==.

---

## 14. Callouts (Obsidian Specific)

Create callouts using `>` followed by `[!TIP]`, `[!WARNING]`, etc.

```markdown
> [!TIP] Helpful Tip  
> This is a helpful tip for you.

> [!WARNING] Warning  
> Proceed with caution!
```

### Result:
> [!TIP] Helpful Tip  
> This is a helpful tip for you.  

> [!WARNING] Warning  
> Proceed with caution!

---

**Happy Markdown Writing in Obsidian! 🚀**
