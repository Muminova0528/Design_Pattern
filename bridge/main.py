from java_developer import JavaDeveloper
from cpp_developer import CppDeveloper
from racing_game import RacingGame
from footbal_game import FootballGame


java = JavaDeveloper()
cpp = CppDeveloper()


racing_java = RacingGame(java)
racing_cpp = RacingGame(cpp)

football_java = FootballGame(java)
football_cpp = FootballGame(cpp)


print(racing_java.develop())
print(racing_cpp.develop())

print(football_java.develop())
print(football_cpp.develop())