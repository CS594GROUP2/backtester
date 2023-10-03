from core.signals import SignalGenerator

signal_generator = SignalGenerator()

entry_probability = .5;
exit_probability = .5;
array_size = 20;

result = signal_generator.random_signals(array_size, entry_probability, exit_probability)

print(result)
