## References

## Notes

##### models.py

Notice how we declared a tuple for **STATUS** of a post to keep draft and published posts separated when we render them out with templates.

The **Meta class inside the model contains metadata.** We tell Django to **sort results in the created_on field in descending** order by default when we query the database. We specify descending order using the **negative prefix**. By doing so, **posts published recently will appear first.**

**What is a “slug” in Django?**

> When I read Django code I often see in models what is called a "slug". I am not quite sure what this is, but I do know it has something to do with URLs. How and when is this slug-thing supposed to be used?

**Ans.** It's a way of generating a valid URL, generally using data already obtained. For instance, using the title of an article to generate a URL. I'd advise to generate the slug, using a function, given a title (or other piece of data), rather than setting it manually.

**An Example:**

```XML
<title> The 46 Year Old Virgin </title>
<content> A silly comedy movie </content>
<slug> the-46-year-old-virgin </slug>
```

Now let's pretend that we have a Django model such as:

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=40)
```

How would you reference this object with a URL, with a meaningful name? You could use Article.id so the URL would look like this:

> www.example.com/article/23

Or, you could reference the title like so:

> www.example.com/article/The 46 Year Old Virgin

Problem is, spaces aren't valid in URLs, they need to be replaced by %20 which is ugly, making it the following:

> www.example.com/article/The%2046%20Year%20Old%20Virgin

That's not solving our meaningful URL. Wouldn't this be better:

> www.example.com/article/the-46-year-old-virgin

That's a slug. the-46-year-old-virgin. All letters are downcased and spaces are replaced by hyphens -. See the URL of this very webpage for an example!

---
