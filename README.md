# py-chess

I try to start doing some scripts on the base of Python and python-chess, to see if development and deployment are going easier than working with Javascript.

The goal here is to provide some tooling that allows people to work with the command line.

The following ideas I have at the moment:

* Analyse games from Lichess automatically (by using a local engine).
* Use that analysis then to find common flaws in the play of a player.
* Provide some tooling / hints to check centipawn losses, and derive from it some information.

I have no idea if that is working without a problem, but the idea is easy enough.

## TODOs

* Find out how to ready games from a study in Lichess.
* Find out how to integrate Stockfish (installed locally).
* Compute centipawn losses per move, and collect the ones (game, then FEN + move) over a threshold.
* Provide the result in an easy to read format:
  * JSON to use with other tools
  * CSV to derive statistics from it
  * Markdown to have an executable report: link to the study, including the position, with the next move and some explanation.
