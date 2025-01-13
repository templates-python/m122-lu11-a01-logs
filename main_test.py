import main

def test(capsys):
    main.calculate()
    captured = capsys.readouterr()
    assert captured.out == "Total: 75.75\n"
