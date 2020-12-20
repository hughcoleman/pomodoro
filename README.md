<h3 align="center">pomodoro</h3>

<p align="center">
  <b>A Pomodoro timer for the command line.</b>
</p>

###### Usage

Run the `pomodoro` script, and pass session options via command-line flags. If no arguments are supplied, program defaults to standard 25m-work/5m-rest cycle. 

```bash
$ pomodoro --work 25 --rest 5
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

To pause or quit the timer, hit `Ctrl-C`.

###### License

[MIT](https://choosealicense.com/licenses/mit/)