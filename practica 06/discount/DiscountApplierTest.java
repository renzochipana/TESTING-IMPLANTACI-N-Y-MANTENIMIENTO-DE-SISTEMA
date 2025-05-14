package tudelft.discount;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.mockito.Mockito;
import java.util.Arrays;
import java.util.List;

public class DiscountApplierTest {
    @Test
    public void applyDiscountsCorrectly() {
        Product homeProduct = new Product("Silla", 100.0, "HOME");
        Product businessProduct = new Product("Laptop", 200.0, "BUSINESS");

        List<Product> products = Arrays.asList(homeProduct, businessProduct);

        ProductDao mockDao = Mockito.mock(ProductDao.class);
        Mockito.when(mockDao.all()).thenReturn(products);

        DiscountApplier applier = new DiscountApplier(mockDao);
        applier.setNewPrices();

        assertEquals(90.0, homeProduct.getPrice(), 0.001);      // 90% de 100
        assertEquals(220.0, businessProduct.getPrice(), 0.001); // 110% de 200
    }
}
