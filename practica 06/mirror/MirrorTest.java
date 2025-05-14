package tudelft.mirror;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MirrorTest {

    @Test
    public void testMirrorEnds_abXYZba() {
        Mirror mirror = new Mirror();
        String result = mirror.mirrorEnds("abXYZba");
        assertEquals("ab", result);
    }

    @Test
    public void testMirrorEnds_abca() {
        Mirror mirror = new Mirror();
        String result = mirror.mirrorEnds("abca");
        assertEquals("a", result);
    }

    @Test
    public void testMirrorEnds_aba() {
        Mirror mirror = new Mirror();
        String result = mirror.mirrorEnds("aba");
        assertEquals("aba", result);
    }

    @Test
    public void testMirrorEnds_empty() {
        Mirror mirror = new Mirror();
        String result = mirror.mirrorEnds("");
        assertEquals("", result);
    }

    @Test
    public void testMirrorEnds_noMatch() {
        Mirror mirror = new Mirror();
        String result = mirror.mirrorEnds("abcde");
        assertEquals("", result);
    }

    @Test
    public void testMirrorEnds_fullMatchEven() {
        Mirror mirror = new Mirror();
        String result = mirror.mirrorEnds("abccba");
        assertEquals("abccba", result);
    }

    @Test
    public void testMirrorEnds_fullMatchOdd() {
        Mirror mirror = new Mirror();
        String result = mirror.mirrorEnds("racecar");
        assertEquals("racecar", result);
    }
}
