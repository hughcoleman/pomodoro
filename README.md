<h3 align="center">pomodoro</h3>

<p align="center">
  <b>A Pomodoro timer for the command line.</b>
</p>

###### Usage

Run the `pomodoro` script, and pass session duration options via command-line flags.

```bash
$ pomodoro [--work WORK_MINUTES=25] [--rest REST_MINUTES=5]
```

The Pomodoro timer will be rendered in your terminal. As time passes, the circle will slowly turn pink. The current activity type is displayed at the bottom.

```
            ....
        _d^^^^^^^^b_
     .d''          ``b.
   .p'                `q.
  .d'                  `b.
 .d'                    `b.
 ::                      ::
 ::       00:13:37       ::
 ::                      ::
 `p.                    .q'
  `p.                  .q'
   `b.      WORK      .d'
     `q..          ..p'
        ^q........p^
            ''''
```

To pause/quit the timer, press `Esc` followed by `p` or `q`, respectively.

###### License

[MIT](https://choosealicense.com/licenses/mit/)
