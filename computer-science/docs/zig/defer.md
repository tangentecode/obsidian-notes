# Defer

Defer is used to execute a statement upon exiting the current block.

```zig
test "defer" {    
	var x: i16 = 5;
	{        
		defer x += 2;
        try expect(x == 5);    
    }    
    try expect(x == 7);
}
```

When there are multiple defers in a single block, they are executed in **reverse order**.

```zig
test "multi defer" {
	var x: f32 = 5;    
	{
	    defer x += 2;        
	    defer x /= 2;    
	}    
	try expect(x == 4.5);
}
```

Defer is useful to ensure that resources are cleaned up when they are no longer needed. Instead of needing to remember to manually free up the resource, you can add a defer statement right next to the statement that allocates the resource.
