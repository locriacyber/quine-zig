Simple quine in Zig inspired by by *Reflections on Trusting Trust* by Ken Thompson.

## How to generate `st`

Copy from the empty line above `const std = @import("std");` to file end, and pass the text through python script like
```sh
xsel | python gen_st.py
```
Then copy the output back to `src/main.zig`