# Flag Checker V2.0

[website](./Flag%20checker.html)

Similar to [Flag Checker V1.0](../FlagCheckerV1.0), upon opening the website, a dialog box asks us to "Enter the flag". When we enter an incorrect flag, we get the response "You got wrong flag". Looking at the source of the web page, we see the JavaScript file main.js. The code is obfuscated, so we beautify and deobfuscate with this online [deobfuscator](https://www.javascriptdeobfuscator.com/). We skim through the code and find this snippet of code containing the logic for the dialog box.

```
var variable_42;
    variable_42 = prompt(_0x5125('0x10', 'D5FN'));
    if (variable_42 == _0x5125('0x11', ']!tO')) {
        alert('You\x20got\x20the\x20right\x20flag');
    } else {
        if (_0x5125('0x12', 'JVHN') !== _0x5125('0x13', 'Jk8w')) {
            alert(_0x5125('0x14', '&lOq'));
        } else {}
    }
```

variable_42 is the input from the dialog box and _0x5125('0x11', ']!tO') is our flag. Let's print that value by running the necessary code to call this function. We can do this in the console of the browser. I used Chrome's console.

```
var _0x5e62 = ['w6R6dQ==', 'MnNb', 'NBEaaMONw5AswonCm3hGwr14X8OUa8OFw7zCtcOpDWE=', 'WHTCiw==', 'dQE8', 'wq0jZw==', 'AAge', 'cV9E', 'w4bCpx8Pw4NzwrAkThnDu3jDlhBVf8OtVVDCl8KNw7U=', 'wqc6w6o=', 'w5DDj8Kfw4VB', 'wo3DjMK3SMK2wqEVw5oPVMKKNcOAEW3DqQ==', 'w63ClMKzwoIYHsOMw7rDiVDClCnChcK6wq8nw7xBEsO/X8KIH3DCnlZQaR5HA8OVwrHDlE0sEVRkwr5fNjPDs8KdwpTCqG4DwrIHbADDqcKDYWV8DcKzwpTDnQ==', 'wrBIO8O1', 'wqXDmxTDoxM=', 'ahNaUQ==', 'fEFdwp5z', 'USzCtA==', 'VzXClw==', 'TsOcPcK9wrw=', 'PsKVQMO2L8O8EMOhHMOOw7sIJsO1', 'Zh9GSMKLScKAK3cwwpLCoHgNwpUIwqMOwqXCusOIWsKPwppGdTo5eRfCrcKRw4/CtHNT', 'w5oWwpk=', 'OwDCgA==', 'w48Jw5oswrkQwpRkBWnCoTLDr1BAw4dgwo/CscKQLw0=', 'CmrCoA==', 'ACJg', 'D8Ozwrc=', 'w7oIwp4=', 'w7fCpTEHwqMVw7DCpGF1w5/DmFLCjEjCpA==', 'wq1ZeGnCnsKzwpDDj33Du0bCvkvDlnDDqDjCl8ONwpbDpcOHRMOBw4E9OFDDp3fCvEw3T1x0wqIqU2R6w7Evw5rDs8OYRsOOGsKIbMKxE8O5QsOaBMK9wpLDqxt6', 'w4xbZnw=', 'Tz3Cixc=', 'w5fDpiHCrA==', 'YXfCkkXCnw==', 'PMKMFcKSwpbDmE5lJ8Ogwpxvw5tUw4g=', 'fwZZScKT', 'FU7ClVTDgA1Ew7HDqULCsg==', 'ehNLUA==', 'wr5BN8Oz', 'wrpHPsOt', 'M8KXGhPDrcOY', 'I8OlMg==', 'QEZh', 'XjTCgQ==', 'ciMKwpPDjMOcw6IXwqcRwr0=', 'w7jCsMKJYQ==', 'w77Cp8Kcf0U=', 'BsOGwpnDpcOJPgU8QgbCpQ==', 'BV7CsQTDpQ==', 'a3bCjEPCnyUlwrNnUMO8', 'w64Jwr4M', 'wqJudl0=', 'WcKDJm5xw7/DpHDDjsKQCQ==', 'VcOKAg=='];
(function(_0x2e4d58, _0x14c882) {
    var _0x18c2d3 = function(_0x28e4b7) {
        while (--_0x28e4b7) {
            _0x2e4d58['push'](_0x2e4d58['shift']());
        }
    };
    _0x18c2d3(++_0x14c882);
}(_0x5e62, 0xa9));
var _0x5125 = function(_0x4d6021, _0x3f8d8b) {
    _0x4d6021 = _0x4d6021 - 0x0;
    var _0x2dfd7f = _0x5e62[_0x4d6021];
    if (_0x5125['initialized'] === undefined) {
        (function() {
            var _0x5307f8 = function() {
                var _0xdd3db6;
                try {
                    _0xdd3db6 = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');')();
                } catch (_0x29e69c) {
                    _0xdd3db6 = window;
                }
                return _0xdd3db6;
            };
            var _0x23f59c = _0x5307f8();
            var _0x48a914 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
            _0x23f59c['atob'] || (_0x23f59c['atob'] = function(_0x206b25) {
                var _0x92d18 = String(_0x206b25)['replace'](/=+$/, '');
                for (var _0x1e27fd = 0x0, _0x20f59d, _0x446dfa, _0x53651c = 0x0, _0x49c025 = ''; _0x446dfa = _0x92d18['charAt'](_0x53651c++); ~_0x446dfa && (_0x20f59d = _0x1e27fd % 0x4 ? _0x20f59d * 0x40 + _0x446dfa : _0x446dfa, _0x1e27fd++ % 0x4) ? _0x49c025 += String['fromCharCode'](0xff & _0x20f59d >> (-0x2 * _0x1e27fd & 0x6)) : 0x0) {
                    _0x446dfa = _0x48a914['indexOf'](_0x446dfa);
                }
                return _0x49c025;
            });
        }());
        var _0x3a355d = function(_0x53f2b0, _0x2b3688) {
            var _0x1ed54c = [],
                _0x5d1d31 = 0x0,
                _0x4734e1, _0x5a14e7 = '',
                _0xc8ab15 = '';
            _0x53f2b0 = atob(_0x53f2b0);
            for (var _0x41e1e2 = 0x0, _0x39eca1 = _0x53f2b0['length']; _0x41e1e2 < _0x39eca1; _0x41e1e2++) {
                _0xc8ab15 += '%' + ('00' + _0x53f2b0['charCodeAt'](_0x41e1e2)['toString'](0x10))['slice'](-0x2);
            }
            _0x53f2b0 = decodeURIComponent(_0xc8ab15);
            for (var _0x4ab6e5 = 0x0; _0x4ab6e5 < 0x100; _0x4ab6e5++) {
                _0x1ed54c[_0x4ab6e5] = _0x4ab6e5;
            }
            for (_0x4ab6e5 = 0x0; _0x4ab6e5 < 0x100; _0x4ab6e5++) {
                _0x5d1d31 = (_0x5d1d31 + _0x1ed54c[_0x4ab6e5] + _0x2b3688['charCodeAt'](_0x4ab6e5 % _0x2b3688['length'])) % 0x100;
                _0x4734e1 = _0x1ed54c[_0x4ab6e5];
                _0x1ed54c[_0x4ab6e5] = _0x1ed54c[_0x5d1d31];
                _0x1ed54c[_0x5d1d31] = _0x4734e1;
            }
            _0x4ab6e5 = 0x0;
            _0x5d1d31 = 0x0;
            for (var _0x388b4a = 0x0; _0x388b4a < _0x53f2b0['length']; _0x388b4a++) {
                _0x4ab6e5 = (_0x4ab6e5 + 0x1) % 0x100;
                _0x5d1d31 = (_0x5d1d31 + _0x1ed54c[_0x4ab6e5]) % 0x100;
                _0x4734e1 = _0x1ed54c[_0x4ab6e5];
                _0x1ed54c[_0x4ab6e5] = _0x1ed54c[_0x5d1d31];
                _0x1ed54c[_0x5d1d31] = _0x4734e1;
                _0x5a14e7 += String['fromCharCode'](_0x53f2b0['charCodeAt'](_0x388b4a) ^ _0x1ed54c[(_0x1ed54c[_0x4ab6e5] + _0x1ed54c[_0x5d1d31]) % 0x100]);
            }
            return _0x5a14e7;
        };
        _0x5125['rc4'] = _0x3a355d;
        _0x5125['data'] = {};
        _0x5125['initialized'] = !![];
    }
    var _0x2669d5 = _0x5125['data'][_0x4d6021];
    if (_0x2669d5 === undefined) {
        if (_0x5125['once'] === undefined) {
            _0x5125['once'] = !![];
        }
        _0x2dfd7f = _0x5125['rc4'](_0x2dfd7f, _0x3f8d8b);
        _0x5125['data'][_0x4d6021] = _0x2dfd7f;
    } else {
        _0x2dfd7f = _0x2669d5;
    }
    return _0x2dfd7f;
};
```

```
_0x5125('0x11', ']!tO')
```
The output is xiomara{0bfu5c@ti0n_@r3_@lw@y5_h@rd}.